from django.shortcuts import render
from django.http import HttpResponse
from rango.forms import UserForm, UserProfileForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import Artist, Album

def home(request):
    return render(request, 'applausable/home.html')

def artist(request):
    #TODO: update query so with filter so it only shows top reviewed
    artist_list = Artist.objects.all()

    context_dict= {'artists': artist_list}
    return render(request, 'applausable/artist.html', context=context_dict)

def album(request):
    return render(request, 'applausable/album.html')    

def show_artist(request, artist_name_slug):
    context_dict = {}

    try:
        artist = Artist.objects.get(slug=artist_name_slug)
        albums = Album.objects.filter(artistID=artist) 

        context_dict['albums'] = album
        context_dict['artist'] = artist 

    except Category.DoesNotExist:
        context_dict['artist'] = None
        context_dict['albums'] = None

    return render(request, 'applausable/artist.html', context=context_dict)

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
                return redirect(reverse('rango:index'))
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
