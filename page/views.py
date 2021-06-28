from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Movie
from page.forms import MovieForm
from .forms import MovieForm


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'page/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'page/movie_detail.html', {'movie': movie})

def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'page/movie_edit.html', {'form': form})