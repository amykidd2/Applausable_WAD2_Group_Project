from django.urls import path
from django.conf.urls import url
from rango import views

app_name = 'applausable'

urlpatterns = [
    path('home/artist/', views.artist, name='artist'),
    path('home/specificArtist/<slug:artist_name_slug>/', views.show_artist, name='show_artist'),
    path('home/album/<slug:album_name_slug>/', views.show_album, name='show_album'),
    path('home/song/<slug:song_name_slug>/', views.show_song, name='show_song'),
    path('user/', views.show_user, name='show_user'),
    path('home/genre/<genre_name>/', views.show_genre, name='show_genre'),
    path('home/allGenres/', views.all_genre, name='all_genre'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('artist/<slug:artist_name_slug>/add_album/', views.add_album, name='add_album'),
    path('album/<slug:album_name_slug>/add_song/', views.add_song, name='add_song'),
    path('song/<slug:song_name_slug>/add_review/', views.add_review, name='add_review'),
    # Accounts templates are being used instead (url link found in other dir)
    #path('logout/', views.logout, name='logout'),
    #path('home/login/', views.login, name='login'),
    #path('home/signup/', views.signup, name='signup'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('searchResults/', views.SearchResultsView, name='search_results'),
    path('highestReviewedSongs/', views.highestReviewedSongs, name='highestReviewedSongs'),
]