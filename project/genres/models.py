from django.db import models

class Genre(models.Model):
    name = models.TextField(verbose_name='Название жанра', null=False)
