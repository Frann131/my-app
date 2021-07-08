from django import forms

from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('originalName', 'nameInSpain', 'year', 'director', 'duration', 'sinopsis', 'genres', 'rate')
        widgets = {
            'originalName': forms.Charinput(attrs={'placeholder': 'Nombre orignal de la pelicula'}),
            'nameInSpain': forms.TextInput(attrs={'placeholder': 'Nombre de la pelicula en España'}),
            'year': forms.TextInput(attrs={'placeholder': 'Año de lanzamiento'}),
            'director': forms.TextInput(attrs={'placeholder': 'Nombre del director'}),
            'duration': forms.positive_small_integer_field(attrs={'placeholder': 'Minutos'}),
            'sinopsis': forms.TextInput(attrs={'placeholder': 'Breve resumen de la trama'}),
            'genres': forms.TextInput(attrs={'placeholder': 'Separados por coma'}),
        }