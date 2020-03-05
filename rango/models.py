from django.db import models

class User(models.Model): 
    username = models.CharField(primary_key=True, max_length=20, unique=True)
    password = models.CharField(max_length=128)
    #TODO: profilePicture
    profile_picture = upload = models.ImageField(upload_to =MEDIA_DIR) 
    professional = models.BooleanField(default=False)
    #TODO: reviews 
    
    def __str__(self): 
        return self.username

class Artist(models.Model): 
    artistID = models.CharField(primary_key=True, max_length=20, unique=True)
    name = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    #TODO: songs
    description = models.CharField(max_length=248)
    LinkToSocialMedia = models.URLField() 

    def __str__(self): 
        return self.artistID

class Song(models.Model): 
    songID = models.CharField(primary_key=True, max_length=20, unique=True)
    title = models.CharField(max_length=128)
    album = models.CharField(max_length=128)
    artistName = models.CharField(max_length=128)
    artistID = models.ForeignKey(Artist, on_delete=models.CASCADE)
    #TODO: reviews
    overallScore = models.IntegerField(default=0)
    linkToSong = models.URLField() 
    
    def __str__(self): 
        return self.songID 

class Review(models.Model): 
    reviewID = models.CharField(primary_key=True, max_length=20, unique=True)
    review = models.CharField(max_length=248)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    songID = models.ForeignKey(Song, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    score = models.IntegerField(default=0)

    
    def __str__(self): 
        return self.reviewID

      