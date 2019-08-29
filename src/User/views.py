import django_filters.rest_framework
from rest_framework import generics, filters
from .models import User, UserSerializer
from rest_auth.registration.views import RegisterView
# from . import permissions


class CustomRegisterView(RegisterView):
    queryset = User.objects.all()


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
