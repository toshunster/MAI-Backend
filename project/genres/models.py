import datetime

from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=32, verbose_name="название")
    is_published = models.BooleanField('активно', default=False)
    date_created = models.DateField('дата создания', default=datetime.datetime.now())

    def __str__(self):
        return f"{self.name}"
