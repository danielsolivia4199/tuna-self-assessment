from django.db import models
from rest_framework import serializers
from .artist import Artist

class Song(models.Model):

    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    album = models.CharField(max_length=50)
    length = models.IntegerField(null=True)
    
def get_genres(self):
        # Retrieve the associated genres for this song
    return self.genres.all()
