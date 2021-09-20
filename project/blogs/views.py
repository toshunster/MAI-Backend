from django.shortcuts import render
from django.http import HttpResponse

def blog_index(request, blog_id):
    print(f"blog_id={blog_id}")
    #return HttpResponse(f'<html><head/><body><h1>Blog #{blog_id}</h1></body></html>')
    context = {'title': f'Пост #{blog_id}', 'description': f'Описание поста №{blog_id}'}
    return render(request, 'blogs/detail.html', context)
