from django.contrib import admin
from . import models


@admin.register(models.Artist)

class ArtistAdmin(admin.ModelAdmin):
	list_display = [
        'artist_name',
        ]



@admin.register(models.Album)

class AlbumAdmin(admin.ModelAdmin):
	list_display = [
        'id', 
        'album_name',
    ]



class SongInlineModel(admin.TabularInline):
    model = models.Song
    fields = [
        'song_name', 
        'type'
        ]


@admin.register(models.Song)

class SongAdmin(admin.ModelAdmin):
    list_display = [
        'song_name', 
        'album',
        'type'
        ]



