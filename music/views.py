from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


'''This was the old code
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Album, Songs
from django.template import loader


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.songs_set.get(pk=request.POST['song'])
    except (KeyError, Songs.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message' : 'You did not select a valid song',
        })
    else:
        selected_song.is_fav = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})


def index_old(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums
    }
    return HttpResponse(template.render(context, request))


def index_oldest(request):
    html = ''
    all_albums = Album.objects.all()
    for album in all_albums:
        url = '/music/'+str(album.id)+'/'
        html+= '<a href="'+url+'">'+ album.album_title+'</a><br>'
    return HttpResponse(html)


def detail_old(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album not found")
    return render(request, 'music/detail.html', {'album': album})

'''