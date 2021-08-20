# Generated by Django 3.2.6 on 2021-08-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
        ('actors', '0002_actor_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(related_name='actors', through='actors.ActorMovie', to='movies.Movie'),
        ),
    ]
