from django.contrib.auth import get_user_model  # new
from rest_framework import serializers

from .models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "subtitle",
            "image",
            "body",
            "minutes_to_read",
            "created_at",
        )
        model = Articles
    

class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)