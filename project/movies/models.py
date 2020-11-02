from django.db import models
from genres.models import Genre

def get_cover_path(instance, filename):
    movie_id = instance.id
    return f"covers/{movie_id}_{filename}"

class Movie(models.Model):
    title = models.CharField(max_length=64, verbose_name="Название фильма")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True, related_name='movies')
    year = models.IntegerField('Год создания', null=True)
    #cover = models.ImageField('Обложка', null=True, blank=True, upload_to='covers')
    cover = models.ImageField('Обложка', null=True, blank=True, upload_to=get_cover_path)

    def __str__(self):
        return f"{self.title} - {self.year}"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
