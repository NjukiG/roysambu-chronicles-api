from django.shortcuts import render

# from rest_framework import generics, permissions  # new
from django.contrib.auth import get_user_model  # new
from rest_framework import viewsets # new
# from rest_framework import generics
from rest_framework.permissions import IsAdminUser  # new

from .models import Articles
from .permissions import IsAuthorOrReadOnly  # new
from .serializers import ArticlesSerializer, UserSerializer  # new


class ArticlesViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class UserViewSet(viewsets.ModelViewSet): # new
    permission_classes = [IsAdminUser] # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer






# class ArticlesList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)  # new
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer

# class ArticlesDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     # permission_classes = (permissions.IsAdminUser,) # new
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer


# class UserList(generics.ListCreateAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# Create your views here.
