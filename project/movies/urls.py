from django.urls import path

from movies.views import movie_index, movies_list, movie_detail, movie_detail_deprecated, movie_add_deprecated
from movies.views import MovieView, MoviesViewsetList, MoviesGenericView

urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('deprecated/<int:movie_id>/', movie_detail_deprecated, name='movie_detail_deprecated'),
    path('deprecated/', movie_add_deprecated, name='movie_add_deprecated'),
    path('<int:movie_id>/', movie_detail, name='movie_detail'),
    path('views/<int:movie_id>/', MovieView.as_view(), name='movie_view'),
    path('viewset/<int:pk>/', MoviesViewsetList.as_view({'get': 'retrieve'}), name='movie_viewset'),
    path('viewset/', MoviesViewsetList.as_view({'get': 'list'}), name='movie_viewset_list'),
    path('generics/', MoviesGenericView.as_view(), name='movie_viewset_generic'),
]
