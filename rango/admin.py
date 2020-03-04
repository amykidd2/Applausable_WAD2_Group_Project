from django.contrib import admin
from rango.models import UserProfile, Artist, Album

admin.site.register(UserProfile) 

#Apparently can't display the forgien key 'artistID'
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('albumID', 'albumName')
admin.site.register(Album, AlbumAdmin)

class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('artistName',)}
    list_display = ('artistID', 'artistName', 'genre', 'description', 'LinkToSocialMedia')
admin.site.register(Artist, ArtistAdmin)
