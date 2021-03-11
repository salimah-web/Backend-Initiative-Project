from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class movie(models.Model):
    Title=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    producer=models.CharField(max_length=30)
    production_year=models.CharField(max_length=4)


    def __str__(self):
        return self.Title

class rentals(models.Model):
    movie_id = models.ForeignKey(to=movie,on_delete=models.CASCADE)
    amount=models.CharField(max_length=10)
    def __str__(self):
        return self.movie_id

    

    