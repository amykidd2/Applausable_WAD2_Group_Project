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
    something_review = [{'reviewID': 1113, 'review': 'Best love song ever written', 'songID': 1013, 'score': 5, 'user': 2},]
    octopus_review = [{'reviewID': 1114, 'review': 'Ringos Best', 'songID': 1014, 'score': 5, 'user': 2},]
    oh_darling_review = [{'reviewID': 1115, 'review': 'Great Sound!', 'songID': 1015, 'score': 5, 'user': 2},]
    letItBe_review = [
        {'reviewID': 1121, 'review': 'My favourite Beatles song', 'songID': 1021, 'score': 5, 'user': 2},
        {'reviewID': 1211, 'review': 'Not for me', 'songID': 1011, 'score': 2, 'user': 2}
    ]
    two_of_us_review = [{'reviewID': 1131, 'review': 'Really good song which I had heard it earlier in my life', 'songID': 1022, 'score': 5, 'user': 2},]
    dig_a_pony_review = [{'reviewID': 1132, 'review': 'Underated Beatles track', 'songID': 1023, 'score': 5, 'user': 2},]
    accross_the_universe_review = [{'reviewID': 1134, 'review': 'Great Song!!!', 'songID': 1024, 'score': 5, 'user': 2},]
    dig_it_review = [{'reviewID': 1135, 'review': 'Its alright', 'songID': 1025, 'score': 5, 'user': 2},]

    wonderwall_review = [
        {'reviewID': 2111, 'review': 'Good but heard it too many times', 'songID': 2011, 'score': 3, 'user': 2}
    ]
    dlbia_review = [
        {'reviewID': 2112, 'review': 'Good.', 'songID': 2012, 'score': 8, 'user': 2}
    ]
    champagne_review = [
        {'reviewID': 2113, 'review': 'Banger', 'songID': 2013, 'score': 7, 'user': 2}
    ]
    hello_review = [
        {'reviewID': 2114, 'review': 'Great track but not the best in the album', 'songID': 2014, 'score': 6, 'user': 2}
    ]
    liveForever_review = [
        {'reviewID': 2121, 'review': 'Not for me', 'songID': 2021, 'score': 1, 'user': 2}
    ]
    rocknroll_review = [
        {'reviewID': 2122, 'review': 'Really good song', 'songID': 2022, 'score': 8, 'user': 2}
    ]

    hcym_review = [
        {'reviewID': 3111, 'review': 'One of the best of the album', 'songID': 3111, 'score': 7, 'user': 2}
    ]
    debasser_review = [
        {'reviewID': 3121, 'review': 'Love the base line!!', 'songID': 3112, 'score': 8, 'user': 2}
    ]
    velouria_review = [
        {'reviewID': 3211, 'review': 'Really great song', 'songID': 3121, 'score': 8, 'user': 2}
    ]
    allison_review = [
        {'reviewID': 3212, 'review': 'One of their finist', 'songID': 3122, 'score': 8, 'user': 2}
    ]
    ns_review = [
        {'reviewID': 4111, 'review': 'One of the classic OK Computer songs', 'songID': 4111, 'score': 8, 'user': 2}
    ]
    let_down_review = [
        {'reviewID': 4112, 'review': 'This is one of the best produced songs Ive ever heard', 'songID': 4112, 'score': 8, 'user': 2}
    ]
    es_review = [
        {'reviewID': 5112, 'review': 'This rocks', 'songID': 5111, 'score': 8, 'user': 2}
    ]

    abbeyRoad_songs = [
        {'songID': 1011, 'title': 'Come Together', 'albumID':1010,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=45cYwDMibGo', 'reviews': comeTogether_review, 'overallScore' : 4, 'genre' : 'Pop'},
        {'songID': 1012, 'title': 'Here Comes The Sun', 'albumID':1010,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=xUNqsfFUwhY', 'reviews': hereComes_review, 'overallScore' : 5, 'genre' : 'Pop'},
        {'songID': 1013, 'title': 'Something', 'albumID':1010,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=UelDrZ1aFeY', 'reviews': something_review, 'overallScore' : 5, 'genre' : 'Pop'},
        {'songID': 1014, 'title': 'Octopuses Garden', 'albumID':1010,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=De1LCQvbqV4', 'reviews': octopus_review, 'overallScore' : 5, 'genre' : 'Pop'},
        {'songID': 1015, 'title': 'Oh! Darling', 'albumID':1010,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=9BznFjbcBVs', 'reviews': oh_darling_review, 'overallScore' : 5, 'genre' : 'Pop'},
        ]
    letItBe_songs = [
        {'songID': 1021, 'title': 'Let It Be', 'albumID':1020,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=QDYfEBY9NM4', 'reviews': letItBe_review, 'overallScore' : 5, 'genre' : 'Pop'},
         {'songID': 1022, 'title': 'Two Of Us', 'albumID':1020,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=cLQox8e9688', 'reviews': two_of_us_review, 'overallScore' : 5, 'genre' : 'Pop'},
         {'songID': 1023, 'title': 'Dig A Pony', 'albumID':1020,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=LpdJE7HG8Ls', 'reviews': dig_a_pony_review, 'overallScore' : 5, 'genre' : 'Pop'},
         {'songID': 1024, 'title': 'Accross The Universe', 'albumID':1020,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=90M60PzmxEE', 'reviews': accross_the_universe_review, 'overallScore' : 5, 'genre' : 'Pop'},
         {'songID': 1025, 'title': 'Dig It', 'albumID':1020,'artistName':'The Beatles', 'artistID': 1000, 'linkToSong':'https://www.youtube.com/watch?v=fUUOX6kAIxI', 'reviews': dig_it_review, 'overallScore' : 6, 'genre' : 'Pop'},
        ]
    wtsmg_songs = [
        {'songID': 2011, 'title': 'Wonderwall', 'albumID':2010,'artistName':'Oasis', 'artistID': 2000, 'linkToSong':'https://www.youtube.com/watch?v=6hzrDeceEKc', 'reviews': wonderwall_review, 'overallScore' : 3, 'genre' : 'Pop'},
        {'songID': 2012, 'title': 'Dont Look Back In Anger', 'albumID':2010,'artistName':'Oasis', 'artistID': 2000, 'linkToSong':'https://www.youtube.com/watch?v=r8OipmKFDeM', 'reviews': dlbia_review, 'overallScore' : 8, 'genre' : 'Pop'},
        {'songID': 2013, 'title': 'Champagne Supernova', 'albumID':2010,'artistName':'Oasis', 'artistID': 2000, 'linkToSong':'https://www.youtube.com/watch?v=tI-5uv4wryI', 'reviews': champagne_review, 'overallScore' : 7, 'genre' : 'Pop'},
        {'songID': 2014, 'title': 'Hello', 'albumID':2010,'artistName':'Oasis', 'artistID': 2000, 'linkToSong':'https://www.youtube.com/watch?v=7HF1Sfos3v4', 'reviews': hello_review, 'overallScore' : 6, 'genre' : 'Pop'},

        ]
    definetlyMaybe_songs = [
        {'songID': 2021, 'title': 'Live Forever', 'albumID':2020,'artistName':'Oasis', 'artistID': 2000, 'linkToSong':'https://www.youtube.com/watch?v=i_2mWhfOhGU', 'reviews': liveForever_review, 'overallScore' : 1, 'genre' : 'Pop'},
        {'songID': 2022, 'title': 'Rock N Roll Star', 'albumID':2020,'artistName':'Oasis', 'artistID': 2000, 'linkToSong':'https://www.youtube.com/watch?v=DMzZcmQ2byc', 'reviews': rocknroll_review, 'overallScore' : 8, 'genre' : 'Pop'}
        ]

    dolittle_songs = [
        {'songID': 3111, 'title': 'Here Comes Your Man', 'albumID':3010,'artistName':'The Pixies', 'artistID': 3000, 'linkToSong':'https://www.youtube.com/watch?v=tPgf_btTFlc', 'reviews': hcym_review, 'overallScore' : 7, 'genre' : 'Rock'},
        {'songID': 3112, 'title': 'Debasser', 'albumID':3010,'artistName':'The Pixies', 'artistID': 3000, 'linkToSong':'https://www.youtube.com/watch?v=PVyS9JwtFoQ', 'reviews': debasser_review, 'overallScore' : 8, 'genre' : 'Rock'}
        ]
    bossonova_songs = [
        {'songID': 3121, 'title': 'Velouria', 'albumID':3020,'artistName':'The Pixies', 'artistID': 3000, 'linkToSong':'https://www.youtube.com/watch?v=nc0Mv4Iyxvc', 'reviews': velouria_review, 'overallScore' : 8, 'genre' : 'Rock'},
        {'songID': 3122, 'title': 'Allison', 'albumID':3020,'artistName':'The Pixies', 'artistID': 3000, 'linkToSong':'https://www.youtube.com/watch?v=pGtnI3EPkKw', 'reviews': allison_review, 'overallScore' : 8, 'genre' : 'Rock'}
        ]
    ok_computer_songs = [
        {'songID': 4111, 'title': 'No Surpises', 'albumID':4010,'artistName':'Radiohead', 'artistID': 4000, 'linkToSong':'https://www.youtube.com/watch?v=u5CVsCnxyXg', 'reviews': ns_review, 'overallScore' : 8, 'genre' : 'Indy'},
        {'songID': 4112, 'title': 'Let Down', 'albumID':4010,'artistName':'RadioHead', 'artistID': 4000, 'linkToSong':'https://www.youtube.com/watch?v=M_wGLZmwZ8o', 'reviews': let_down_review, 'overallScore' : 8, 'genre' : 'Indy'}
        ]

    metallica_songs = [
        {'songID': 5111, 'title': 'Enter Sandman', 'albumID':5010,'artistName':'Metallica', 'artistID': 5000, 'linkToSong':'https://www.youtube.com/watch?v=CD-E-LDc384', 'reviews': es_review, 'overallScore' : 8, 'genre' : 'Metal'},
        
        ]
    beatles_albs =[
        {'albumID': 1010, 'albumName': 'Abbey Road','songs':abbeyRoad_songs, 'albumCover':'album_covers/abbey_road.jpg'},
        {'albumID': 1020, 'albumName': 'Let It Be', 'songs':letItBe_songs, 'albumCover':'album_covers/let_it_be.png'}
    ]
     
    oasis_albs = [
        {'albumID': 2010, 'albumName': '(Whats the Story) Morning Glory?', 'artistID':2000,'songs':wtsmg_songs, 'albumCover':'album_covers/wtsmg.jpg'},
        {'albumID': 2020, 'albumName': 'Definetly Maybe','artistID':2000,'songs':definetlyMaybe_songs, 'albumCover':'album_covers/definetly_maybe.jpg'}
    ]

    pixies_albs = [
        {'albumID': 3010, 'albumName': 'Dolittle', 'artistID':3000,'songs':dolittle_songs, 'albumCover':'album_covers/download.jpg'},
        {'albumID': 3020, 'albumName': 'Bossonova','artistID':3000,'songs':bossonova_songs, 'albumCover':'album_covers/bossonova.jpg'}
    ]

    radiohead_albs = [
        {'albumID': 4010, 'albumName': 'OK Computer', 'artistID':4000,'songs':ok_computer_songs, 'albumCover':'album_covers/ok_computer.jpg'},
    ]

    metallica_albs= [
        {'albumID': 5010, 'albumName': 'Metallica', 'artistID':5000,'songs':metallica_songs, 'albumCover':'album_covers/metallica.jpg'},
    ]
     
    arts = {
        1000 : {'albs': beatles_albs, 'artistName': 'The Beatles', 'genre': 'rock', 'description': 'John, Paul, George and Ringo', 'LinkToSocialMedia': 'https://www.youtube.com/user/thebeatles', 'artistImage':'artist_images/the_beatles.jpg'}, 
        2000 : {'albs': oasis_albs, 'artistName': 'Oasis', 'genre': 'rock', 'description': 'Liam, Noel, Paul, Paul and Tony', 'LinkToSocialMedia': 'https://www.youtube.com/user/oasisinetofficial','artistImage':'artist_images/oasis.jpg'},
        3000 : {'albs': pixies_albs, 'artistName': 'The Pixies', 'genre': 'Rock', 'description': 'Black Francis and the band are Rock icons', 'LinkToSocialMedia': 'https://www.pixiesmusic.com/','artistImage':'artist_images/unnamed.jpg'},
        4000 : {'albs': radiohead_albs, 'artistName': 'Radiohead', 'genre': 'Indy', 'description': 'Thom York, Johnny Greenwood, Phillip Selway and the others', 'LinkToSocialMedia': 'https://www.radiohead.co.uk/','artistImage':'artist_images/Radiohead.jpg'},
        5000 : {'albs': metallica_albs, 'artistName': 'Metallica', 'genre': 'Metal', 'description': 'The pivital metal band', 'LinkToSocialMedia': 'https://www.metallica.com/','artistImage':'artist_images/metallica.jpg'},
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