# from django.db import models
from django.conf import settings
from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=250)
    image = models.URLField(max_length=500)
    body = models.TextField()
    minutes_to_read = models.IntegerField(default=5)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

# Create your models here.
