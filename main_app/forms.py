from django.forms import ModelForm
from .models import Song

class SongForm(ModelForm):
  class Meta:
    model = Song
    fields = ['title', 'artist', 'album', 'year', 'song_url']