from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=200 )
    image=models.CharField(max_length=1000 ,default="please enter the image URL here")
    age=models.IntegerField( default=0  )
    nationality=models.CharField(max_length=200,default='Canaidian')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.artist_name

   
                      
class Album(models.Model):
    album_name = models.CharField(max_length=200,default="New Album")
    artist= models.ForeignKey(Artist, on_delete=models.DO_NOTHING,default=0)
    rate = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return self.album_name

        

class Song(models.Model):

# specifying choices

    CHOICES = (
        (0, _('classical')),
        (1, _('hip-hop')),
        (2, _('soul')),
        (3, _('folk')),
        (4, _('rock')),
        (5,_('romantic'))
    )

    TYPE = (
        (0, _('Multiple Choice')),
    )

    song_name = models.CharField(max_length=200, verbose_name=_("Song Name"))
    album = models.ForeignKey(Album, on_delete=models.DO_NOTHING, default=0)
    type =models.IntegerField(
        choices = CHOICES,
        verbose_name=_("Type"),
        default = '1'
        )
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.song_name
        