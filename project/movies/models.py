from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=64)

class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField()
