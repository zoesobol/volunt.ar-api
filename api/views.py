'''
from django.shortcuts import render
from rest_framework import generics
from . import models
from .serializers import UserSerializer

# Create your views here.

class UserView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
'''
