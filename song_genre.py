from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import SongGenre, SongGenreSerializer

class SongGenreView(ViewSet):
  
    """"Tuna API Song Genres View"""   
    def retrieve(self, request, pk):
        """"Handle GET requests for single song genre
        """
        
        song_genre = SongGenre.objects.get(pk=pk)
        serializer = SongGenreSerializer(song_genre)
        return Response(serializer.data)  
      
 
    def list(self, request):
        """Handle GET requests to get all song genres
        
        Returns:
            Response -- JSON serialized list of song genres
        """
        
        
        song_genres = SongGenre.objects.all()
        serializer = SongGenreSerializer(song_genres, many=True)
        return Response(serializer.data)  
    
