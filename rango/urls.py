from django.urls import path
from rango import views

app_name = 'applausable'

urlpatterns = [
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
]