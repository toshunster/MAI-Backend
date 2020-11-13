from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from .views import login_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blogs/', include('blog.urls')),
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social')),
    #path('api/movies/', include('movies.urls')),
]
