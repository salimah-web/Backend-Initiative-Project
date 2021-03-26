from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class movie(models.Model):
    Title=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    producer=models.CharField(max_length=30)
    production_year=models.CharField(max_length=4)
    rent_fee =models.CharField(max_length=10, default='2000')

    def __str__(self):
        return self.Title

class rentals(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, default = 1)
    movie_id = models.ForeignKey(movie,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.movie_id)