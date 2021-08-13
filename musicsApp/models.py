from django.db import models
from django.db.models.enums import Choices

# Create your models here.


class Artist(models.Model):
    artist_name = models.CharField(max_length=200 ,default=0)
    artist_age=models.IntegerField(max_length=200 , default=0  )
    artist_nationality=models.CharField(max_length=200,default='spain')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.artist_name

class Album(models.Model):
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    albums_name = models.CharField(max_length=200)
    rate = models.IntegerField(default=0)
    def __str__(self):
        return self.albums_name

class Song(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
    song_type = models.CharField(max_length=200, choices=((1,'romantic'),(2,'rock'),(3,'soul')), default=1)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.song_name
        