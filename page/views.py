from django.shortcuts import render
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'page/movie_list.html', {'movies': movies})