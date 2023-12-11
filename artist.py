from django.db import models
from rest_framework import serializers

class Artist(models.Model):

    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    bio = models.CharField(max_length=50)


