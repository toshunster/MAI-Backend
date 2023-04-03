from datetime import datetime

from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название жанра', null=True)

class Movie(models.Model):
    category = models.ForeignKey(Genre, on_delete=models.SET_NULL, verbose_name='жанр', null=True)
    title = models.CharField(max_length=64, verbose_name='Название фильма', null=True, unique=False)
    added_at = models.DateTimeField(verbose_name='Дата добавления', default=datetime.now)
    year = models.IntegerField(verbose_name='Год', null=True)
