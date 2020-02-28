from django.contrib import admin
from rango.models import User, Artist, Song, Review, Album

admin.site.register(User) 
admin.site.register(Artist)
admin.site.register(Song) 
admin.site.register(Review)
admin.site.register(Album)
