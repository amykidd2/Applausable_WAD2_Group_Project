from django.db import models
from django.contrib.auth.models import User    

class Artist(models.Model): 
    artistID = models.CharField(primary_key=True, max_length=20, unique=True)
    name = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    description = models.CharField(max_length=248)
    LinkToSocialMedia = models.URLField() 

    def __str__(self): 
        return self.artistID

class Album(models.Model):
    artistID = models.ForeignKey(Artist, on_delete=models.CASCADE)
    ablumID = models.CharField(primary_key=True, max_length=20, unique=True)
    albumName = models.CharField(max_length=128)

    def __str__(self): 
        return self.albumID

#In book they have a seperate UserProfile which links to django's User model instead
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True, editable=True)  

    def __str__(self): 
        return self.user.username         