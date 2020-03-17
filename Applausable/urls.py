"""Applausable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rango import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'applausable'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('home/artist/', views.artist, name='artist'),
    path('home/specificArtist/<slug:artist_name_slug>/', views.show_artist, name='show_artist'),
    path('home/album/<slug:album_name_slug>/', views.show_album, name='show_album'),
    path('home/song/<slug:song_name_slug>/', views.show_song, name='show_song'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('artist/<slug:artist_name_slug>/add_album/', views.add_album, name='add_album'),
    path('album/<slug:album_name_slug>/add_song/', views.add_song, name='add_song'),
    path('home/login/', views.login, name='login'),
    path('home/signup/', views.signup, name='signup'),
    # Made a restricted page just cause rango has one in the book just in case we want to use it
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
