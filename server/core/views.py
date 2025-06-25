from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    """
    View to register a new user.
    """
    serializer_class = UserSerializer
