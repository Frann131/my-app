from django.urls import path
from . import views
from .forms import MovieForm

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/new', views.movie_new, name='movie_new'),
]