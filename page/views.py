from django.shortcuts import render

def movie_list(request):
    return render(request, 'page/movie_list.html', {})