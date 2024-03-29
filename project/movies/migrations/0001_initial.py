# Generated by Django 4.0 on 2023-03-20 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название жанра')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, null=True, verbose_name='Название фильма')),
                ('added_at', models.DateTimeField(default=1679330029.9636211, verbose_name='Дата добавления')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.genre', verbose_name='жанр')),
            ],
        ),
    ]
