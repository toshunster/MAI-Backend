from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название фильма')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name='Жанр')
    year = models.IntegerField(verbose_name='Год релиза')
    original_title = models.CharField(max_length=128, null=True, verbose_name='Оригинальное название', help_text='Название фильма на оригинальном языке')
    cover = models.ImageField(upload_to='movies_cover/', null=True, verbose_name='Обложка для фильма')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['title']
#class MovieHelper(models.Model):
#    my_super_pk1 = models.AutoField(primary_key=True)
#    my_super_pk2 = models.CharField(max_length=64, primary_key=True)
#    title = models.CharField(max_length=128)
