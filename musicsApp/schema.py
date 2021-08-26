import graphene
from graphene_django import DjangoObjectType
from .models import Artist,Album,Song


class ArtistsType(DjangoObjectType):
    class Meta:
        model=Artist
        fields = "__all__"



class AlbumsType(DjangoObjectType):
    class Meta:
        model=Album
        fields = "__all__"


class SongsType(DjangoObjectType):
    class Meta:
        model=Song
        fields = "__all__"



class Query(graphene.ObjectType):
    
    all_artists=graphene.List(ArtistsType)
    all_albums=graphene.List(AlbumsType)
    all_songs=graphene.List(SongsType)

    def resolve_all_artists(root,info,):
        return Artist.objects.all()
    def resolve_all_albums(root,info):
        return Album.objects.all()
    def resolve_all_songs(root,info):
        return Song.objects.all()


schema = graphene.Schema(query=Query)