from django.db import models
from django.contrib.auth.models import User    

class Category(models.Model):
    name_max_length = 128
    name = models.CharField(max_length=name_max_length, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Page(models.Model):
    page_max_length = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=page_max_length) 
    url = models.URLField() 
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title 

#In book they have a seperate UserProfile which links to django's User model instead
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True, editable=True)  

    def __str__(self): 
        return self.user.username         