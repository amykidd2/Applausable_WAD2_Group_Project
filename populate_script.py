import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Applausable.settings') 
 
import django 
django.setup() 

from rango.models import Artist, Album, Song, Review, User


def populate():

    comeTogether_review = [
        {'reviewID': 1111, 'review': 'A classic', 'songID': 1011, 'score': 4, 'user': 2},
        {'reviewID': 1221, 'review': 'Good but reminds me of my ex boyfriend', 'songID': 1021, 'score': 3, 'user': 2}
    ]
    hereComes_review = [
        {'reviewID': 1112, 'review': 'Cured my depression', 'songID': 1012, 'score': 5, 'user': 2},
        {'reviewID': 1212, 'review': 'My fave ever', 'songID': 1012, 'score': 5, 'user': 2}
    ]
    letItBe_review = [
        {'reviewID': 1121, 'review': 'My favourite Beatles song', 'songID': 1021, 'score': 5, 'user': 2},
        {'reviewID': 1211, 'review': 'Not for me', 'songID': 1011, 'score': 2, 'user': 2}
    ]
    wonderwall_review = [
        {'reviewID': 2111, 'review': 'Good but heard it too many times', 'songID': 2011, 'score': 3, 'user': 2}
    ]
    liveForever_review = [
        {'reviewID': 2121, 'review': 'Not for me', 'songID': 2021, 'score': 1, 'user': 2}
    ]

    abbeyRoad_songs = [
        {'songID': 1011, 'title': 'Come Together', 'albumID':1010,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=45cYwDMibGo', 'reviews': comeTogether_review, 'overallScore' : 4, 'genre' : 'Pop'},
        {'songID': 1012, 'title': 'Here Comes The Sun', 'albumID':1010,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=xUNqsfFUwhY', 'reviews': hereComes_review, 'overallScore' : 5, 'genre' : 'Pop'}
        ]
    letItBe_songs = [
        {'songID': 1021, 'title': 'Let It Be', 'albumID':1020,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=QDYfEBY9NM4', 'reviews': letItBe_review, 'overallScore' : 5, 'genre' : 'Pop'}
        ]
    wtsmg_songs = [
        {'songID': 2011, 'title': 'Wonderwall', 'albumID':2010,'artistName':'Oasis', 'artistID': 2000, 'linkToSong':'https://www.youtube.com/watch?v=6hzrDeceEKc', 'reviews': wonderwall_review, 'overallScore' : 3, 'genre' : 'Pop'}
        ]
    definetlyMaybe_songs = [
        {'songID': 2021, 'title': 'Live Forever', 'albumID':2020,'artistName':'Oasis', 'artistID': 2000, 'linkToSong':'https://www.youtube.com/watch?v=i_2mWhfOhGU', 'reviews': liveForever_review, 'overallScore' : 1, 'genre' : 'Pop'}
        ]


    beatles_albs =[
        {'albumID': 1010, 'albumName': 'Abbey Road','songs':abbeyRoad_songs, 'albumCover':'album_covers/abbey_road.jpg'},
        {'albumID': 1020, 'albumName': 'Let It Be', 'songs':letItBe_songs, 'albumCover':'album_covers/let_it_be.png'}
    ]
     
    oasis_albs = [
        {'albumID': 2010, 'albumName': '(Whats the Story) Morning Glory?', 'artistID':2000,'songs':wtsmg_songs, 'albumCover':'album_covers/wtsmg.jpg'},
        {'albumID': 2020, 'albumName': 'Definetly Maybe','artistID':2000,'songs':definetlyMaybe_songs, 'albumCover':'album_covers/definetly_maybe.jpg'}
    ]
     
    arts = {
        1000 : {'albs': beatles_albs, 'artistName': 'The Beatles', 'genre': 'rock', 'description': 'John, Paul, George and Ringo', 'LinkToSocialMedia': 'https://www.youtube.com/user/thebeatles', 'artistImage':'artist_images/the_beatles.jpg'}, 
        2000 : {'albs': oasis_albs, 'artistName': 'Oasis', 'genre': 'rock', 'description': 'Liam, Noel, Paul, Paul and Tony', 'LinkToSocialMedia': 'https://www.youtube.com/user/oasisinetofficial','artistImage':'artist_images/oasis.jpg'}
    }
     
    
    user = User(username='defaultUserName', email='default_user@gmail.com', password='defaultPassword123')
    user.save()
    for arts, arts_data in arts.items():
        a = add_artist(arts, arts_data['artistName'], arts_data['genre'], arts_data['description'], arts_data['LinkToSocialMedia'], arts_data['artistImage'])
        for album in arts_data['albs']:
            alb = add_album(a, album['albumID'], album['albumName'], album['albumCover'])
            for song in album['songs']:
                s = add_song(song['songID'], song['title'], alb, a, song['linkToSong'], song['artistName'], song['overallScore'], song['genre'])
                for r in song['reviews']:
                    add_review(r['reviewID'], r['review'], s, r['score'], user)
    
    
    #Doesn't seem to want to print it out in command line but doesn't effect the actual population        
    #for a in Artist.objects.all():
        #for alb in Album.objects.filter(artistID=a):
            #print(f'- {a}: {alb}')

def add_review(reviewID, review, song, score, user):
    r = Review.objects.get_or_create(reviewID=reviewID,songID=song, user=user)[0]
    r.review=review
    r.score=score
    r.user = user
    r.save()
    return r

def add_song(songID, title, alb, a, linkToSong, artistName, overallScore, genre):
    song = Song.objects.get_or_create(songID=songID,albumID=alb,artistID=a)[0]
    song.title=title
    song.artistName = artistName
    song.linkToSong = linkToSong
    song.overallScore = overallScore
    song.genre = genre
    song.save()
    return song

def add_album(arts, albumID, albumName, albumCover):
    alb = Album.objects.get_or_create(artistID=arts, albumID=albumID)[0]
    alb.albumName=albumName
    alb.albumCover = albumCover
    alb.save()
    return alb

def add_artist(artistID, artistName, genre, description, LinkToSocialMedia, artistImage):
    a = Artist.objects.get_or_create(artistID=artistID)[0]
    a.artistName=artistName
    a.genre=genre
    a.description=description
    a.LinkToSocialMedia=LinkToSocialMedia
    a.artistImage = artistImage
    a.save()
    return a

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()