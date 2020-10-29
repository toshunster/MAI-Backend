from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({'posts': serializer.data})

    def post(self, request):
        # ...
        return Response({'error': None, 'result': 'Пост успешно добавлен'})

def blog_info(request):
    return render(request, 'base.html', { 'guest': 'Anton' })

def blog_view(request, pk):
    return HttpResponse(f'<html><h1>Blog #{pk}</h1></html>')
