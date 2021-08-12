from django.db.models import fields
from rest_framework import serializers
from .models import Artist,Album,Song



class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Artist


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Album


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Song