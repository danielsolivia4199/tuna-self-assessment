from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, SongSerializer

class SongView(ViewSet):
  
    """"Tuna API Songs View"""   
    def retrieve(self, request, pk):
        """"Handle GET requests for single song
        """
        
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)  
      
 
    def list(self, request):
        """Handle GET requests to get all artists
        
        Returns:
            Response -- JSON serialized list of artists
        """
        
        
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
