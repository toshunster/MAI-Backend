from django.db import models
from genres.models import Genre

class Movie(models.Model):
    title = models.CharField(max_length=64, verbose_name="Название фильма")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True, related_name='movies')
    year = models.IntegerField(null=True, blank=True, verbose_name="Год")
