from django.shortcuts import render
from django.http import HttpResponse


def movie_index(request):
    return HttpResponse('Hello, movies')

def movie_page(request):
    return render(request, 'base.html', {})
