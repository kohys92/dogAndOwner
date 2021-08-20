from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=45)
    release_date=models.DateField()
    running_time=IntegerField()

    class Meta:
        db_table="movies"