from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Artist,Album,Song
from .serializers import AlbumSerializer , ArtistSerializer , SongSerializer

# Create your views here.

class ArtistList(APIView):

    def get(self,request):
        artist1=Artist.objects.all()
        serializer=ArtistSerializer(artist1, many=True)
        return Response(serializer.data)


class ArtistDetail(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer




class AlbumList(APIView):
    def get(self,request):
        album1=Album.objects.all()
        serializer=AlbumSerializer(album1, many=True)
        return Response(serializer.data)


class AlbumDetail(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer




class SongList(APIView):
    def get(self,request):
        song1=Song.objects.all()
        serializer=SongSerializer(song1, many=True)
        return Response(serializer.data)


class SongDetail(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer