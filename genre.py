from django.db import models
from rest_framework import serializers

class Genre(models.Model):
    
    description = models.CharField(max_length=50)
    
    
    
