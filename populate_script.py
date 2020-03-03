import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Applausable.settings') 
 
import django 
django.setup() 
from rango.models import Artist, Album

def populate():
    beatles_albs =[
        {'albumID': 1010, 'albumName': 'Abbey Road'},
        {'albumID': 1020, 'albumName': 'Let It Be'}
    ]         #just now image is set as null
     
    oasis_albs = [
        {'albumID': 2010, 'albumName': '(Whats the Story) Morning Glory?'},
        {'albumID': 2020, 'albumName': 'Definetly Maybe'}
    ]         #just now image is set as null
     
    arts = {
        1000 : {'albs': beatles_albs, 'name': 'The Beatles', 'genre': 'rock', 'description': 'John, Paul, George and Ringo', 'linkToSocialMedia': 'https://www.youtube.com/user/thebeatles'}, 
        2000 : {'albs': oasis_albs, 'name': 'Oasis', 'genre': 'rock', 'description': 'Liam, Noel, Paul, Paul and Tony', 'linkToSocialMedia': 'https://www.youtube.com/user/oasisinetofficial'}
    }
     
    for arts, arts_data in arts.items():
        a = add_artist(arts, arts_data['name'], arts_data['genre'], arts_data['description'], arts_data['linkToSocialMedia'])
        for alb in arts_data['albs']:
            add_album(a, alb['albumID'], alb['albumName'])
             
    for a in Artist.objects.all():
        for alb in Album.objects.filter(artistID=a):
            print(f'- {a}: {alb}')


def add_album(arts, albumID, albumName, artistID):
    alb = Album.objects.get_or_create(artistID=arts, albumID=albumID)[0]
    alb.albumName=albumName
    alb.artistID=artistID
    alb.save()
    return alb

def add_artist(artistID, name, genre, description, linkToSocialMedia):
    a = Artist.objects.get_or_create(name=name)[0]
    a.artistId=artistID
    a.genre=genre
    a.description=description
    a.linkToSocialMedia=linkToSocialMedia
    a.save()
    return a

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()    
