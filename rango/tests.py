from django.test import TestCase
from rango.models import Song, Album, Artist, Review, User
from django.urls import reverse
from rango.forms import UserForm, UserProfileForm, ArtistForm, AlbumForm, SongForm, ReviewForm


#class SongMethodTests(TestCase):
  #  def test_ensure_overallScore_is_between_0_and_10(self):
       # artist = Artist.objects.get(slug='oasis')
      #  album = Album.objects.get(artistID=artist) 
     #   """
    #    Ensures the number of views received for a Category are positive or zero.   
   ##     """
  #      song = Song(title='test', songID=10000, artistID= artist, albumID=album, overallScore=11, artistName = 'The Tests', genre = 'Pop', linkToSong = 'http:www.test.com', songImage = 'test.jpg')
 #       song.save()
#        self.assertEqual((song.overallScore >=10), False)




class ArtistMethodTests(TestCase):
    def test_slug_line_creation(self):
        
        artist = Artist(artistName='Random Artist String')
        artist.save()
        self.assertEqual(artist.slug, 'random-artist-string')

    def test_add_artist_page_view_without_login(self):
        response = self.client.get(reverse('applausable:add_artist'))
        self.assertEqual(response.status_code, 302) #302 is an authentication error


class HomeViewTests(TestCase):
    def test_home_view_with_no_artist(self):
        
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no artists present.')
        self.assertQuerysetEqual(response.context['artists'], [])

class HighestRatedSongsViewTest(TestCase):
    def test_highest_rated_songs_view_with_no_songs(self):
        response = self.client.get(reverse('applausable:highestReviewedSongs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No songs availble')
        self.assertQuerysetEqual(response.context['songs'], [])

class UserViewTest(TestCase):
    def test_user_page_view_without_login(self):
        response = self.client.get(reverse('applausable:show_user'))
        self.assertEqual(response.status_code, 302) #302 is an authentication error
        
