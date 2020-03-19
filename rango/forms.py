from django import forms
from rango.models import UserProfile, Artist, Album, Song, Review
from django.contrib.auth.models import User  
from django.core.validators import MinValueValidator, MaxValueValidator

class ArtistForm(forms.ModelForm):
    artistID = forms.IntegerField(widget=forms.HiddenInput(), initial=0000)
    artistName = forms.CharField(max_length=128, help_text='Enter artist name.')
    genre = forms.CharField(max_length=128, help_text='Enter genre.')
    description = forms.CharField(max_length=248, help_text='Enter your artist description.')
    LinkToSocialMedia = forms.URLField(help_text='Enter your social media link.')
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    #slug = forms.SlugField(widget=forms.HiddenInput(), required=False,unique=True, default=uuid.uuid1)
    class Meta:
        model = Artist
        
        fields = ('artistName', 'genre', 'description', 'LinkToSocialMedia' )

class AlbumForm(forms.ModelForm):
    #albumID = forms.IntegerField(widget=forms.HiddenInput(), initial=0000) #this doesnt work for some reason it just makes it 0 rather than increasing it.
    albumName = forms.CharField(max_length=128, help_text='Enter the album name')
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Album

# What fields do we want to include in our form?
# This way we don't need every field in the model present.
# Some fields may allow NULL values; we may not want to include them.
# Here, we are hiding the foreign key.
# we can either exclude the category field from the form,
        exclude = ('artistID', 'albumID')
# or specify the fields to include (don't include the category field).
#fields = ('title', 'url', 'views')


class SongForm(forms.ModelForm):
    #songID = forms.IntegerField(widget=forms.HiddenInput(), initial=0000)
    title = forms.CharField(max_length=128, help_text='Enter the song title')
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    artistName = forms.CharField(max_length=128, help_text = 'Enter the name of the artist')
    overallScore = forms.IntegerField(widget=forms.HiddenInput(), initial=0000)
    linkToSong = forms.CharField(help_text='Enter youtube link to song')
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Song

# What fields do we want to include in our form?
# This way we don't need every field in the model present.
# Some fields may allow NULL values; we may not want to include them.
# Here, we are hiding the foreign key.
# we can either exclude the category field from the form,
        exclude = ('artistID', 'albumID', 'songID')
# or specify the fields to include (don't include the category field).
#fields = ('title', 'url', 'views')


class ReviewForm(forms.ModelForm):

    review = forms.CharField(max_length=248, help_text='Enter your review')
    score = forms.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)], initial=0, help_text='Enter your score')
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Review

# What fields do we want to include in our form?
# This way we don't need every field in the model present.
# Some fields may allow NULL values; we may not want to include them.
# Here, we are hiding the foreign key.
# we can either exclude the category field from the form,
        exclude = ('songID','reviewID')
# or specify the fields to include (don't include the category field).
#fields = ('title', 'url', 'views')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)