from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now=True)
    rating = models.SmallIntegerField()