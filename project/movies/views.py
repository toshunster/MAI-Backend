# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def movie_index(request):
    return HttpResponse('Hello, movies')
