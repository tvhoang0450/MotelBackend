from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, )
from rest_framework.decorators import api_view
from rest_framework import serializers


class MyProfile(APIView):

    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get(seft, request, *args, **kwargs):
        user = get_object_or_404(User, pk = request.user.id)
        serializer = UserSerializer(user)
        return Response({"profile": serializer.data})

    @csrf_exempt
    def put(seft, request, *args, **kwargs):
        profile = get_object_or_404(User, pk = request.user.id)
        data = request.data.get('userprofile')
        serializer = UserSerializer(instance=profile, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            profile_saved = serializer.save()
        return Response({"success": "Profile '{}' updated successfully".format(profile_saved.id)})


    

    
class ProfileUpdateDeleteAPIView(viewsets.GenericViewSet,
                                  RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


