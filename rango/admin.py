from django.contrib import admin
from rango.models import UserProfile, Artist, Song, Review, Album

admin.site.register(UserProfile) 
admin.site.register(Artist)
admin.site.register(Song) 
admin.site.register(Review)
admin.site.register(Album)
