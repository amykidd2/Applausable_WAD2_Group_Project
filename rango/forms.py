from django import forms
from rango.models import UserProfile, Artist
from django.contrib.auth.models import User  

class ArtistForm(forms.ModelForm):
    artistID = forms.IntegerField(widget=forms.HiddenInput(), initial=0000)
    artistName = forms.CharField(max_length=128, help_text='Enter artist name.')
    genre = forms.CharField(max_length=128, help_text='Enter genre.')
    description = forms.CharField(max_length=248, help_text='Enter your artist description.')
    LinkToSocialMedia = forms.URLField(help_text='Enter your social media link.')
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Artist
        fields = ('artistName', 'genre', 'description', 'LinkToSocialMedia' )
        #when doing album
        #exclude = ('artistID')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)