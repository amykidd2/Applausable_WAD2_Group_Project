from django.shortcuts import render
from django.http import HttpResponse
from rango.forms import UserForm, UserProfileForm, ArtistForm, AlbumForm, SongForm, ReviewForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import Artist, Album, Song, Review
from registration.backends.simple.views import RegistrationView
from rango.bing_search import run_query
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.db.models import Avg
from django.conf import settings
    
def home(request):
    artist_list = Artist.objects.all()
    context_dict = {}
    context_dict['artists'] = artist_list
    return render(request, 'applausable/home.html', context = context_dict)

def SearchResultsView(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(artistName__icontains=query)

            results= Artist.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'applausable/search_results.html', context)

        else:
            return render(request, 'applausable/search_results.html.html')

    else:
        return render(request, 'applausable/search_results.html.html')

def artist(request):
    #TODO: update query so with filter so it only shows top reviewed
    artist_list = Artist.objects.all()
    album_list = Album.objects.all()
    context_dict = {}
    context_dict['artists'] = artist_list
    context_dict['albums'] = album_list
    return render(request, 'applausable/artist.html', context=context_dict)

def album(request):
    return render(request, 'applausable/album.html')    

def show_artist(request, artist_name_slug):
    context_dict = {}

    try:
        artist = Artist.objects.get(slug=artist_name_slug)
        albums = Album.objects.filter(artistID=artist) 
        songs = Song.objects.filter(artistID= artist)
        context_dict['albums'] = albums
        context_dict['artist'] = artist 
        context_dict['songs'] = songs

    except Category.DoesNotExist:
        context_dict['artist'] = None
        context_dict['albums'] = None

    return render(request, 'applausable/specificArtist.html', context=context_dict)

def show_album(request, album_name_slug):
    context_dict = {}

    try:
        album = Album.objects.get(slug=album_name_slug)
        songs = Song.objects.filter(albumID= album)
        context_dict['album'] = album
        context_dict['songs'] = songs

    except Category.DoesNotExist:
        context_dict['album'] = None
        context_dict['songs'] = None

    return render(request, 'applausable/album.html', context=context_dict)


def show_song(request, song_name_slug):
    context_dict = {}

    try:
        song = Song.objects.get(slug= song_name_slug)
        reviews = Review.objects.filter(songID=song)
        overallScore = Review.objects.filter(songID=song).aggregate(Avg('score'))
        album = song.albumID
        context_dict['album'] = album
        context_dict['song'] = song
        context_dict['link'] = song.linkToSong
        context_dict['reviews'] = reviews
        context_dict['overallScore'] = overallScore

    except Category.DoesNotExist:
        context_dict['album'] = None
        context_dict['song'] = None

    return render(request, 'applausable/song.html', context=context_dict)

def add_artist(request):
    form = ArtistForm()
    
    if request.method == 'POST': 
        form = ArtistForm(request.POST, request.FILES)
        
        if form.is_valid():
            artist = form.save(commit=True)
            #artist.artistImage = form.cleaned_data['artistImage']

            return redirect('/')
        
        else:
            print(form.errors)

    return render(request, 'applausable/add_artist.html', context = {'form': form})

def add_album(request, artist_name_slug):
    try:
        artist = Artist.objects.get(slug=artist_name_slug)
        mostRecentAlbum = Album.objects.order_by('-albumID')[:1]
        previousAlbum = Album.objects.get(albumID=mostRecentAlbum)
    except Artist.DoesNotExist:
        artist = None
        # You cannot add a page to a Category that does not exist...
    if artist is None:
        return redirect('/')

    form = AlbumForm()

    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            if artist:
                album = form.save(commit=False)
                album.artistID = artist 
                album.albumID = previousAlbum.albumID + 1
                album.save()
                return redirect(reverse('applausable:show_artist',
                kwargs={'artist_name_slug':
                artist_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'artist': artist}
    return render(request, 'applausable/add_album.html', context=context_dict)

def add_song(request, album_name_slug):
    try:
        album = Album.objects.get(slug=album_name_slug)
        mostRecentSong = Song.objects.order_by('-songID')[:1]
        previousSong = Song.objects.get(songID=mostRecentSong)
    except Album.DoesNotExist:
        album = None
        # You cannot add a page to a Category that does not exist...
    if album is None:
        return redirect('/')

    form = SongForm()

    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            if album:
                song = form.save(commit=False)
                song.songID = previousSong.songID + 1
                song.artistID = album.artistID
                song.albumID = album
                song.save()
                return redirect(reverse('applausable:show_album',
                kwargs={'album_name_slug':
                album_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'album': album}
    return render(request, 'applausable/add_song.html', context=context_dict)

def add_review(request, song_name_slug):
    try:
        song = Song.objects.get(slug=song_name_slug)
        mostRecentReview = Review.objects.order_by('-reviewID')[:1]
        previousReview = Review.objects.get(reviewID=mostRecentReview)
    except Song.DoesNotExist:
        song = None
        # You cannot add a page to a Category that does not exist...
    if song is None:
        return redirect('/')

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if song:
                review = form.save(commit=False)
                review.songID = song
                review.reviewID = previousReview.reviewID + 1
                review.save()
                return redirect(reverse('applausable:show_song',
                kwargs={'song_name_slug':
                song_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'song': song}
    return render(request, 'applausable/add_review.html', context=context_dict)

def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True  

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'applausable/signup.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}) 

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('applausable: home')) 
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'applausable/login.html') 

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def logout(request):
    logout(request)
    return redirect(reverse('applausable:home'))

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/home/' 

def search(request):
    result_list = []
    
    if request.method == 'POST':
        query = request.POST['query'].strip() 
        if query: 
            # Run our Bing function to get the results list! 
            result_list = run_query(query)

    return render(request, 'applausable/search.html', {'result_list': result_list})