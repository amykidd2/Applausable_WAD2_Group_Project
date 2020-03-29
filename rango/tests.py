from django.test import TestCase
from rango.models import Song, Album, Artist, Review, User
from django.urls import reverse


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
        """
        Checks to make sure that when a category is created, an
        appropriate slug is created.
        Example: "Random Artist String" should be "random-artist-string".
        """
        artist = Artist(artistName='Random Artist String')
        artist.save()
        self.assertEqual(artist.slug, 'random-artist-string')

class AlbumMethodTests(TestCase):
    def test_slug_line_creation(self):
        artist = Artist(artistName='Random Artist String')
        artist.save()

        album = Album(artistID = artist.artistID, albumName='Random Album String')
        album.save()
        self.assertEqual(album.slug, 'random-artist-album-random-artist-string')

class HomeViewTests(TestCase):
    def test_home_view_with_no_artist(self):
        """
        If no categories exist, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no artists present.')
        self.assertQuerysetEqual(response.context['artists'], [])
