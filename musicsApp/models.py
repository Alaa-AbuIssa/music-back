from django.db import models
from django.db.models.enums import Choices



# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=200 )
    artist_image_URL=models.CharField(max_length=1000 ,default="please enter the image URL here")
    artist_age=models.IntegerField(max_length=200 , default=0  )
    artist_nationality=models.CharField(max_length=200,default='Canaidian')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.artist_name



  
# specifying choices
  
SEMESTER_CHOICES = (
    ( "romantic" ,"1-romantic"),
    ( "rock", "2-rock"),
    ("soul","3-soul"),
    ("classical","4-classical"),
    ("folk","5-folk"),
    ("hip hop","6-hip hop")
)

class Album(models.Model):
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE,default=0)
    albums_name = models.CharField(max_length=200)
    rate = models.IntegerField(default=0)
    def __str__(self):
        return self.albums_name

        

class Song(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, default=0)
    song_name = models.CharField(max_length=200)
    song_type =models.CharField(
        max_length = 20,
        choices = SEMESTER_CHOICES,
        default = '1'
        )
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.song_name
        