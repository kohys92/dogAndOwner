from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    date_of_birth=models.DateField()
    movies = models.ManyToManyField("movies.Movie", through="ActorMovie", related_name="actors")

    class Meta:
        db_table='actors'

class ActorMovie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)

    class Meta:
        db_table='actor_movies'