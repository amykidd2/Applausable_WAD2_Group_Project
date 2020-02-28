import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Applausable.settings')

import django
django.setup()
from rango.models import User, Artist, Song, Review, Album

def populate():
    arts = [{
        'id': 1000, 'name': 'The Beatles', 'genre': 'Rock', 
        'albums': {'Abbey Road': {'ablums': abbey_road}}, 
        'description': 'John, Paul, George and Ringo', 
        'linkToSocialMedia': 'https://www.youtube.com/user/thebeatles'
        }]

    abbey_road = [{
        'id': 1010, 'songs': {'Here Comes The Sun': {'songs': here_comes_the_sun}},
        'albumName': 'Abbey Road'
        #TODO: artistID and just now image is set as null
    }]

    here_comes_the_sun = [{
        'id': 1011, 'title' = 'Here Comes The Sun', 'album': 'Abbey Road', 
        'artist': 'The Beatles', 'genre': 'Rock', 'linkToSong': 'https://www.youtube.com/watch?v=bgiQD56eWDk'
        #TODO: artistID and reviews. OverallScore set to 0

    }]

    users = [
        {'userID': 54321, 'password': 12345,'professional': False},
        {'userID': 12345, 'password': 54321, 'professional': True}
        #TODO: add image
        ]


def add_user(userID, password, professional):
    u = User.objects.get_or_create(userID=userID)[0]
    u.password=password
    u.professional=professional
    u.save()
    return u

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
