from django.contrib import admin
from rango.models import UserProfile, Artist, Album

admin.site.register(UserProfile) 
admin.site.register(Artist)
admin.site.register(Album)
