from django.shortcuts import render
from django.http import HttpResponse


def main_view(request):
    return HttpResponse('Hello from main view')

