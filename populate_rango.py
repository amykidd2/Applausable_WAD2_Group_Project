import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Applausable.settings')

import django
django.setup()
from rango.models import User, Artist, Song, Review, Album

def populate():
    arts = [{
        'id': 1000, 'name': 'The Beatles', 'genre': 'Rock', 
        'albums': {'albums': beatles_albs}, 
        'description': 'John, Paul, George and Ringo', 
        'linkToSocialMedia': 'https://www.youtube.com/user/thebeatles'
        }]

    beatles_albs = [
        {'id': 1010, 'songs': {'Here Comes The Sun': {'songs': here_comes_the_sun}},
        'albumName': 'Abbey Road'}
        {'id': 1020, 'songs': {'Let it be': {'songs': let_it_be}},
        'albumName': 'Let It Be'}
        #TODO: artistID and just now image is set as null
    ]

    abbey_road_songs = [{
        'id': 1011, 'title' = 'Here Comes The Sun', 'album': 'Abbey Road', 
        'artist': 'The Beatles', 'genre': 'Rock', 
        'linkToSong': 'https://www.youtube.com/watch?v=bgiQD56eWDk'
        #TODO: artistID and reviews. OverallScore set to 0

    }]


    here_comes_the_sun = [{
        'id': 1011, 'title' = 'Here Comes The Sun', 'album': 'Abbey Road', 
        'artist': 'The Beatles', 'genre': 'Rock', 
        'linkToSong': 'https://www.youtube.com/watch?v=bgiQD56eWDk'
        #TODO: artistID and reviews. OverallScore set to 0

    }]

    abbey_road = [
        {'id': 1010, 'songs': {'Here Comes The Sun': {'songs': here_comes_the_sun}},
        'albumName': 'Abbey Road'}
        ]

    the_beatles = [{
        'id': 1000, 'name': 'The Beatles', 'genre': 'Rock', 
        'albums': {'albums': abbey_road}, 
        'description': 'John, Paul, George and Ringo', 
        'linkToSocialMedia': 'https://www.youtube.com/user/thebeatles'
        }]    


    users = [
        {'userID': 54321, 'password': 12345,'professional': False},
        {'userID': 12345, 'password': 54321, 'professional': True}
        #TODO: add image
        ]

def add_artist(id, name, genre, albums, description, linkToSocialMedia):
    a = Page.objects.get_or_create(id=id, albums=albums)[0]

def add_user(userID, password, professional):
    u = User.objects.get_or_create(userID=userID)[0]
    u.password=password
    u.professional=professional
    u.save()
    return u

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
