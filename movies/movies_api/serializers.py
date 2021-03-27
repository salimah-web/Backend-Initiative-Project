from rest_framework import serializers
from .models import movie,rentals
from django.contrib.auth.models import User
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=movie
        fields=['id','Title','genre','production_year','producer','rent_fee']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length= 6, write_only=True)
    email=serializers.EmailField(max_length=255, min_length=6)
    

    class Meta:
        model = User
        fields=['username','email', 'password']


    def validate_email(self, attrs):
    
        if User.objects.filter(email=attrs).exists():
            raise serializers.ValidationError({'email already exist'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class Rentalserializer(serializers.ModelSerializer):
    movie_Title=serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()
    class Meta:
        model=rentals
        fields=['movie_id','amount','movie_Title']

    def get_movie_Title(self, obj):
        return obj.movie.Title

    def get_amount(self, obj):
        return obj.movie_id.rent_fee

    