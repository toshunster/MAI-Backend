from django.contrib import admin
from genres.models import Genre

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('is_published', 'date_created',)

admin.site.register(Genre, GenreAdmin)

