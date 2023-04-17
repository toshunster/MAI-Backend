# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View

from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView

from movies.models import Genre, Movie
from movies.serializers import MovieSerializer

def movie_index(request):
    movies = Movie.objects.all()
    return HttpResponse(f'Hello, movies: [{"|".join(str(movie) for movie in movies)}]')

def movie_detail_deprecated(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return JsonResponse({'movie': {'id': movie.id, 'title': movie.title, 'year': movie.year}})

def movies_list(request):
    movies = Movie.objects.all()
    return JsonResponse({'movies': list(movies)})

def movie_add_deprecated(request):
    pass

def movies_destroy(request):
    pass

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return JsonResponse({'movie': MovieSerializer(movie).data})

class MovieView(View):
    def get(self, request, movie_id):
        print(f"[MovieView] Method GET")
        movie = get_object_or_404(Movie, id=movie_id)
        return JsonResponse({'movie': MovieSerializer(movie).data})

    def post(self, request, movie_id):
        print(f"[MovieView] Method POST")
        movies = Movie.objects.all()
        return JsonResponse({'movie': MovieSerializer(movies, many=True).data})

class MoviesViewsetList(viewsets.ViewSet):
    def list(self, request):
        movies = Movie.objects.all()
        return JsonResponse({'movie': MovieSerializer(movies, many=True).data})

    def retrieve(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        return JsonResponse({'movie': MovieSerializer(movie).data})

class MoviesGenericView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
