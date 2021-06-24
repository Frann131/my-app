from django import forms

from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('originalName', 'nameInSpain', 'year', 'director', 'duration', 'sinopsis', 'genres', 'rate')