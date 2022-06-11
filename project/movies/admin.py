from django.contrib import admin
from movies.models import Movie, Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'original_title',)
    list_filter = ('year',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
