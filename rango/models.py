from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Artist(models.Model): 
    artistID = models.IntegerField(primary_key=True, unique=True)
    artistName = models.CharField(max_length=128, default='Artist')
    genre = models.CharField(max_length=128, default='Genre')
    description = models.CharField(max_length=248, default='Description')
    LinkToSocialMedia = models.URLField(default='Link')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.artistName)
        super(Artist, self).save(*args, **kwargs)

    def __str__(self): 
        return self.artistID

class Album(models.Model):
    albumID = models.IntegerField(primary_key=True, unique=True)
    albumName = models.CharField(max_length=128)
    artistID = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self): 
        return self.albumID

class Song(models.Model): 
    songID = models.IntegerField(primary_key=True,  unique=True)
    title = models.CharField(max_length=128, default='Title')
    albumID = models.ForeignKey(Album, on_delete=models.CASCADE)
    artistName = models.CharField(max_length=128, default='ArtistName')
    artistID = models.ForeignKey(Artist, on_delete=models.CASCADE)
    overallScore = models.IntegerField(default=0)
    linkToSong = models.URLField() 

    def str(self): 
        return self.songID



#In book they have a seperate UserProfile which links to django's User model instead
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True, editable=True)  

    def __str__(self): 
        return self.user.username