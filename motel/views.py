from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import decorators, authenticate, login
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework import permissions
from .models import TypeMotel, baseInforMotel, Service, Board, ImageMotel
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, )


from .serializers import MotelSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .filters import PhongTroFilterSet


def index(request):
    return HttpResponse("Đây là đài tiếng nói Việt Nam")


class PhongTroListCreateAPIView(viewsets.GenericViewSet,
                                ListCreateAPIView, ):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = (FileUploadParser,)

    serializer_class = MotelSerializer
    queryset = baseInforMotel.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
    def post(self, request, filename, format=None):
        file_obj = request.data['file']
        print(file_obj)


    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = PhongTro.objects.all()
    #     username = self.request.query_params.get('username', None)
    #     if username is not None:
    #         queryset = queryset.filter(owner=username)
    #     return queryset


class PhongTroUpdateDeleteAPIView(viewsets.GenericViewSet,
                                  RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = baseInforMotel.objects.all()
    serializer_class = MotelSerializer
    lookup_field = 'id'


class PhongTroList(generics.ListAPIView):
    queryset = baseInforMotel.objects.all()
    serializer_class = MotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['typeMotel', 'district', 'ward', 'price', 'DienTich']

# class PhongTroViewSet(viewsets.ModelViewSet):
#     queryset = PhongTro.objects.all()
#     serializer_class = PhongTroSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#     filterset_class = PhongTroFilterSet
