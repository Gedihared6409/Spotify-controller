from django.db import models

# Create your models here.
from django.db import models
from api.models import Room


class SpotifyToken(models.Model):
    user = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=10000)
    access_token = models.CharField(max_length=10000)
    expires_in = models.DateTimeField(blank=True, null=True)
    token_type = models.CharField(max_length=10000)


class Vote(models.Model):
    user = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    song_id = models.CharField(max_length=50)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
