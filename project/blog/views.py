from django.shortcuts import render

from django.http import HttpResponse

def blog_info(request):
    return render(request, 'base.html', { 'guest': 'Anton' })

def blog_view(request, pk):
    return HttpResponse(f'<html><h1>Blog #{pk}</h1></html>')
