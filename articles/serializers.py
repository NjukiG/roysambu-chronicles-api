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