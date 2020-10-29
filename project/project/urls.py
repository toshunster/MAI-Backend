from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blogs/', include('blog.urls')),
    #path('api/movies/', include('movies.urls')),
]
