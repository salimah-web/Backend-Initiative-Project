from django.contrib import admin

# Register your models here.
from .models import movie,rentals



admin.site.register(movie)
admin.site.register(rentals)