from django.db import models

from genres.models import Genre

class Movie(models.Model):
    name = models.TextField(verbose_name='Название фильма', null=False, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    genre2 = models.ForeignKey('genres.Genre', on_delete=models.CASCADE, related_name="genre2", null=True)
    year = models.IntegerField(verbose_name='Год', default=2021)
    cover = models.ImageField(null=True, verbose_name='Обложка')

    def __str__(self):
        return f"{self.name}, {self.year} ({self.genre})"
