from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .serializers import MovieSerializer,UserSerializer,Rentalserializer
from django.contrib.auth.models import User
from .models import movie,rentals
from django.http import Http404


class UsersAPIView(APIView):
    
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MovieListAPIView(APIView):
    
    def get(self, request, format=None):
        movies = movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieDetailView(APIView):
    
    def get_object(self, id):
        try:
            return movie.objects.get(id=id)
        except movie.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        movie = self.get_object(id)
        movie.delete()
        return Response({'message':'successfully deleted'},status=status.HTTP_204_NO_CONTENT)

class RentalsView(APIView):
   
    def get(self, request, format=None):
        rental = rentals.objects.all()
        serializer = Rentalserializer(rental, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Rentalserializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentalDetailView(APIView):
    
    def get_object(self, id):
        try:
            return rentals.objects.get(id=id)
        except movie.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        rental = self.get_object(id)
        serializer = Rentalserializer(rental)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        rental = self.get_object(id)
        serializer = RentalSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        rental = self.get_object(id)
        rental.delete()
        return Response({'message':'successfully deleted'},status=status.HTTP_204_NO_CONTENT)
   