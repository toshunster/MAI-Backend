# Generated by Django 2.2 on 2020-11-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AddField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers', verbose_name='Обложка'),
        ),
    ]
