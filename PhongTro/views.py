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
from .models import PhongTro
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, )

from .serializers import PhongTroSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
    return HttpResponse("Đây là đài tiếng nói Việt Nam")


class PhongTroListCreateAPIView(viewsets.GenericViewSet,
                                ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PhongTroSerializer
    queryset = PhongTro.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PhongTroUpdateDeleteAPIView(viewsets.GenericViewSet,
                                  RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    queryset = PhongTro.objects.all()
    serializer_class = PhongTroSerializer
    lookup_field = 'id'

class PhongTroList(generics.ListAPIView):
    queryset = PhongTro.objects.all()
    serializer_class = PhongTroSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['DichVu__TenDV', 'TinhTp__TenTinh' , 'HuyenQuan__TenHuyen', 'Gia', 'DienTich']
    filterset_fields = ['DichVu__TenDV']

class ModelByMakerList(generics.ListAPIView):
    serializer_class = PhongTroSerializer

    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        dichvu = self.kwargs['DichVu']
        return PhongTro.objects.filter(DichVu=dichvu)