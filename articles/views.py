from django.shortcuts import render

# from rest_framework import generics, permissions  # new
from rest_framework import generics

from .models import Articles
from .permissions import IsAuthorOrReadOnly  # new
from .serializers import ArticlesSerializer


class ArticlesList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

class ArticlesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    # permission_classes = (permissions.IsAdminUser,) # new
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

# Create your views here.
