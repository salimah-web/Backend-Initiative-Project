from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import movieSerializer,userSerializer,rentalserializer
from django.contrib.auth.models import User
from moviesapi.models import movie,rentals
@api_view()
@permission_classes([AllowAny])
def first_view(request):
    print(request.query_params)
    return Response({'message':'you are welcome!'})


class users(viewsets.ModelViewSet):
    serializer_class=userSerializer

    def get_queryset(self):
        users=User.objects.all()
        return users

    

class movies(viewsets.ModelViewSet):
    queryset=movie.objects.all()
    serializer_class = movieSerializer


    def destroy(self, request, *args, **kwargs):
        movie_to_del= self.get_object()
        movie_to_del.delete()

        return  Response({'message':'successfully deleted'})

class movie_rentals(viewsets.ModelViewSet):
    queryset=rentals.objects.all()
    serializer_class = rentalserializer

    def destroy(self, request, *args, **kwargs):
        rental_to_del= self.get_object()
        rental_to_del.delete()

        return  Response({'message':'successfully deleted'})



