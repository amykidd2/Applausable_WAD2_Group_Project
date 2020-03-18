import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Applausable.settings') 
 
import django 
django.setup() 

from rango.models import Artist, Album, Song, Review


def populate():

    comeTogether_review = [
        {'reviewID': 1111, 'review': 'A classic', 'songID': 1011, 'score': 4}
    ]
    letItBe_review = [
        {'reviewID': 1121, 'review': 'My favourite Beatles song', 'songID': 1021, 'score': 5}
    ]
    wonderwall_review = [
        {'reviewID': 2111, 'review': 'Good but heard it too many times', 'songID': 2011, 'score': 3}
    ]
    liveForever_review = [
        {'reviewID': 2121, 'review': 'Not for me', 'songID': 2021, 'score': 1}
    ]

    abbeyRoad_songs = [
        {'songID': 1011, 'title': 'Come Together', 'albumID':1010,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=45cYwDMibGo', 'reviews': comeTogether_review}
        ]
    letItBe_songs = [
        {'songID': 1021, 'title': 'Let It Be', 'albumID':1020,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=QDYfEBY9NM4', 'reviews': letItBe_review}
        ]
    wtsmg_songs = [
        {'songID': 2011, 'title': 'Wonderwall', 'albumID':2010,'artistName':'Oasis', 'artistID': 2000, 'linkToSong':'https://www.youtube.com/watch?v=6hzrDeceEKc', 'reviews': wonderwall_review}
        ]
    definetlyMaybe_songs = [
        {'songID': 2021, 'title': 'Live Forever', 'albumID':2020,'artistName':'Oasis', 'artistID': 2000, 'linkToSong':'https://www.youtube.com/watch?v=i_2mWhfOhGU', 'reviews': liveForever_review}
        ]


    beatles_albs =[
        {'albumID': 1010, 'albumName': 'Abbey Road','songs':abbeyRoad_songs},
        {'albumID': 1020, 'albumName': 'Let It Be', 'songs':letItBe_songs}
    ]
     
    oasis_albs = [
        {'albumID': 2010, 'albumName': '(Whats the Story) Morning Glory?', 'artistID':2000,'songs':wtsmg_songs},
        {'albumID': 2020, 'albumName': 'Definetly Maybe','artistID':2000,'songs':definetlyMaybe_songs}
    ]
     
    arts = {
        1000 : {'albs': beatles_albs, 'artistName': 'The Beatles', 'genre': 'rock', 'description': 'John, Paul, George and Ringo', 'LinkToSocialMedia': 'https://www.youtube.com/user/thebeatles'}, 
        2000 : {'albs': oasis_albs, 'artistName': 'Oasis', 'genre': 'rock', 'description': 'Liam, Noel, Paul, Paul and Tony', 'LinkToSocialMedia': 'https://www.youtube.com/user/oasisinetofficial'}
    }
     
    for arts, arts_data in arts.items():
        a = add_artist(arts, arts_data['artistName'], arts_data['genre'], arts_data['description'], arts_data['LinkToSocialMedia'])
        for album in arts_data['albs']:
            alb = add_album(a, album['albumID'], album['albumName'])
            for song in album['songs']:
                add_song(song['songID'], song['title'], alb, a, song['linkToSong'], song['artistName'])
                for r in song['reviews']:
                    add_review(r['reviewID'], r['review'], song, r['score'])
    
    
    #Doesn't seem to want to print it out in command line but doesn't effect the actual population        
    #for a in Artist.objects.all():
        #for alb in Album.objects.filter(artistID=a):
            #print(f'- {a}: {alb}')

def add_review(reviewID, review, song, score):
    r = Review.objects.get_or_create(reviewID=reviewID,songID=song)[0]
    r.review=review
    r.score=score
    r.save()
    return r

def add_song(songID, title, alb, a, linkToSong, artistName):
    song = Song.objects.get_or_create(songID=songID,albumID=alb,artistID=a)[0]
    song.title=title
    song.artistName = artistName
    song.linkToSong = linkToSong
    song.save()
    return song

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