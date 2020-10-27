from django.db import models

class Post(models.Model):
    my_super_pk = models.AutoField(primary_key=True)
    title = models.CharField('Название поста', null=False, max_length=128)
