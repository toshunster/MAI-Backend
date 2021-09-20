from django.urls import path, re_path

from movies.views import MovieView

urlpatterns = [
    path('', MovieView.as_view()),
]
