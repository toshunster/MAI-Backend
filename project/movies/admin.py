from django.contrib import admin
from movies.models import Genre, Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year',)
    list_filter = ('year',)
    list_editable = ('genre',)
    raw_id_fields = ('genre',)
    search_fields = ('title',)

admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
