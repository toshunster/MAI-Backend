from datetime import datetime

from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название жанра', null=True)

    def __str__(self):
        return f"{self.name} ({self.id})"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, verbose_name='жанр', null=True)
    title = models.CharField(max_length=64, verbose_name='Название фильма', null=True, unique=False, help_text='Какая-то полезная информация о названии фильма.')
    added_at = models.DateTimeField(verbose_name='Дата добавления', default=datetime.now)
    year = models.IntegerField(verbose_name='Год', null=True)

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre.name}"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ('added_at',)
