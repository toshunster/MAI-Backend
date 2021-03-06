# Generated by Django 2.0 on 2020-10-12 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 10, 12, 14, 13, 50, 964626), verbose_name='дата создания'),
        ),
        migrations.AddField(
            model_name='genre',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='активно'),
        ),
    ]
