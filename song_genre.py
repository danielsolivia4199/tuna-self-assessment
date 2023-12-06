from django.db import models
from .genre import Genre
from .song import Song

class SongGenre(models.Model):

    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
