from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class Artist(models.Model): 
    artistID = models.IntegerField(primary_key=True, unique=True)
    artistName = models.CharField(max_length=128, default='Artist')
    genre = models.CharField(max_length=128, default='Genre')
    description = models.CharField(max_length=248, default='Description')
    LinkToSocialMedia = models.URLField(default='Link') #sorry I made it a capital L but now I've done too much to change it back
    #slug = models.SlugField(unique=True, )
    artistImage = models.ImageField(upload_to= settings.MEDIA_DIR,default='artist.jpg')
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.artistName)
        super(Artist, self).save(*args, **kwargs)

    def __str__(self): 
        return self.artistID

class Album(models.Model):
    albumID = models.IntegerField(primary_key=True, unique=True)
    albumName = models.CharField(max_length=128)
    artistID = models.ForeignKey(Artist, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    albumCover = models.ImageField(upload_to= 'album_covers/',default='default_album.jpg')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.albumName + self.artistID.artistName)
        super(Album, self).save(*args, **kwargs)

    def __str__(self): 
        return self.albumID

class Song(models.Model): 
    GENRE_CHOICES = (
    ('Pop','POP'),
    ('Rock', 'ROCK'),
    ('Metal','METAL'),
    ('Soul','SOUL'),
    ('Electronic','ELECTRONIC'),
    ('R&B', 'R&B'),
    ('Reggae', 'REGGAE'),
    ('Hip-Hop','HIP-HOP'),
    ('Indie','INDIE'),
    ('Classical','CLASSICAL'),
    ('Country','COUNTRY'),
    ('Jazz','JAZZ'),
)
    songID = models.IntegerField(primary_key=True,  unique=True)
    title = models.CharField(max_length=128, default='Title')
    albumID = models.ForeignKey(Album, on_delete=models.CASCADE)
    artistName = models.CharField(max_length=128, default='ArtistName')
    artistID = models.ForeignKey(Artist, on_delete=models.CASCADE)
    linkToSong = models.CharField(max_length=248, default = 'link') 
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    overallScore = models.IntegerField(default=0)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES, default='Pop')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + self.albumID.albumName)
        super(Song, self).save(*args, **kwargs)
    #should we have a track number? Like the number on the album?

    def str(self): 
        return self.songID

class Review(models.Model): 
    reviewID = models.IntegerField(primary_key=True, unique=True)
    review = models.CharField(max_length=248, default= 'Review')
    #user = models.ForeignKey(User, on_delete=models.CASCADE) implement later
    songID = models.ForeignKey(Song, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(10)])
    user = models.ForeignKey(User, default = 2, on_delete=models.CASCADE)

    def __str__(self): 
        return self.reviewID

#In book they have a seperate UserProfile which links to django's User model instead
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True, editable=True)  

    def __str__(self): 
        return self.user.username