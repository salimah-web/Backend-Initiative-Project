from rest_framework import serializers
from moviesapi.models import movie,rentals
from django.contrib.auth.models import User
class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model=movie
        fields=['Title','genre','production_year','producer']

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class rentalserializer(serializers.ModelSerializer):
    movie_Title=serializers.SerializerMethodField()
    
    class Meta:
        model=rentals
        fields=['movie_id','amount','movie_Title']

    def get_movie_Title(self, obj):
        return obj.movie_id.Title