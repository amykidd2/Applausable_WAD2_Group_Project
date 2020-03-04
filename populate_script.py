import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Applausable.settings') 
 
import django 
django.setup() 
from rango.models import Artist, Album

def populate():

    #TODO: add songs the albs list and update all of the populate
    beatles_albs =[
        {'albumID': 1010, 'albumName': 'Abbey Road'},
        {'albumID': 1020, 'albumName': 'Let It Be'}
    ]
     
    oasis_albs = [
        {'albumID': 2010, 'albumName': '(Whats the Story) Morning Glory?'},
        {'albumID': 2020, 'albumName': 'Definetly Maybe'}
    ]
     
    arts = {
        1000 : {'albs': beatles_albs, 'artistName': 'The Beatles', 'genre': 'rock', 'description': 'John, Paul, George and Ringo', 'LinkToSocialMedia': 'https://www.youtube.com/user/thebeatles'}, 
        2000 : {'albs': oasis_albs, 'artistName': 'Oasis', 'genre': 'rock', 'description': 'Liam, Noel, Paul, Paul and Tony', 'LinkToSocialMedia': 'https://www.youtube.com/user/oasisinetofficial'}
    }
     
    for arts, arts_data in arts.items():
        a = add_artist(arts, arts_data['artistName'], arts_data['genre'], arts_data['description'], arts_data['LinkToSocialMedia'])
        for alb in arts_data['albs']:
            add_album(a, alb['albumID'], alb['albumName'])

    #Doesn't seem to want to print it out in command line but doesn't effect the actual population        
    #for a in Artist.objects.all():
        #for alb in Album.objects.filter(artistID=a):
            #print(f'- {a}: {alb}')


def add_album(arts, albumID, albumName):
    alb = Album.objects.get_or_create(artistID=arts, albumID=albumID)[0]
    alb.albumName=albumName
    alb.save()
    return alb

def add_artist(artistID, artistName, genre, description, LinkToSocialMedia):
    a = Artist.objects.get_or_create(artistID=artistID)[0]
    a.artistName=artistName
    a.genre=genre
    a.description=description
    a.LinkToSocialMedia=LinkToSocialMedia
    a.save()
    return a

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()