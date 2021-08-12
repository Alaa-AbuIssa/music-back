from django.urls import path

from .views import AlbumDetail, ArtistList,SongDetail,ArtistDetail,AlbumList,SongList

urlpatterns = [
    path('artist/', ArtistList.as_view(), name='artist_list'),
    path('album/', AlbumList.as_view(), name='artist_list'),
    path('song/', SongList.as_view(), name='artist_list'),
    path("<int:pk>/", ArtistDetail.as_view(), name='artist_details'),
    path("album/<int:pk>/", AlbumDetail.as_view(), name='album_details'),
    path("song/<int:pk>/", SongDetail.as_view(), name='song_details'),

]