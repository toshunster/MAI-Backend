from django.urls import path

from .views import blog_index

urlpatterns = [
    path('<int:blog_id>/', blog_index),
]
