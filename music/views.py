from django.http import HttpResponse
from django.shortcuts import render

from music.forms import ArtistForm, AlbumForm
from music.models import Artist, Album

def index(request):
    artists = Artist.objects.all()
    context = {'artists': artists}
    return render(request, 'music/index.html', context)


def artist_detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
    else:
        form = ArtistForm(instance=artist)
    context = {'artist': artist, 'form': form}
    return render(request, 'music/artist_detail.html', context)

def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
    else:
        form = AlbumForm(instance=album)
    context = {'album': album, 'form': form}
    return render(request, 'music/album_detail.html', context)

#extra, se puede poner altiro el artists_view
def artists_view(request):
    artists = Artist.objects.all()
    context = {'artists': artists}
    return render(request, 'music/artists.html', context)

#extra, se puede poner altiro el albums_view, para esta parte invoque a ambas tablas
def albums_view(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    context = {'artists': artists, 'album': albums}
    return render(request, 'music/albums.html', context)