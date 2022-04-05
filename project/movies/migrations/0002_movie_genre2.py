# Generated by Django 3.0 on 2021-10-04 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genre2', to='genres.Genre'),
        ),
    ]