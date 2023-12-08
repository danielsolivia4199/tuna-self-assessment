from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artist, ArtistSerializer, SongSerializer

class ArtistView(ViewSet):
  
    """"Tuna API Artists View"""   
    def retrieve(self, request, pk):
        """"Handle GET requests for single artist
        """
        
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistsSongSerializer(artist)
        return Response(serializer.data)  
      
 
    def list(self, request):
        """Handle GET requests to get all artists
        
        Returns:
            Response -- JSON serialized list of artists
        """
        
        
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)  
    

class ArtistsSongSerializer(serializers.ModelSerializer):
    """JSON serializer for artist's songs"""
    songs = SongSerializer(many=True, read_only=True)
    
    class Meta:
        model = Artist
        fields = ('id', 'name', 'age', 'bio', 'songs', )
        depth = 1
