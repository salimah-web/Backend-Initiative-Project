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






# @api_view(['GET'])
# def movie_list(request):
#     movies=movie.objects.all()
#     serializer=movieSerializer(movies,many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def movie_detail(request,pk):
#     movies=movie.objects.get(id=pk)
#     serializer=movieSerializer(movies,many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def movie_create(request):
#     serializer=movieSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def movie_update(request,pk):
#     movies=movie.objects.get(id=pk)
#     serializer=movieSerializer(instance=movies, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data) 

# @api_view(['DELETE'])
# def movie_delete(request,pk):
#     movies=movie.objects.get(id=pk)
#     movies.delete()
#     return Response({'message':'successfuly deleted'})


# @api_view(['GET'])
# def rental_list(request):
#     rental=rentals.objects.all()
#     serializer=rentalserializer(rental,many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def rental_detail(request,pk):
#     rental=rentals.objects.get(id=pk)
#     serializer=rentalserializer(rental,many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_rental(request):
#     serializer=rentalserializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def update_rental(request,pk):
#     rental=rentals.objects.get(id=pk)
#     serializer=rentalserializer(instance=rental, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data) 

# @api_view(['DELETE'])
# def delete_rental(request,pk):
#     rental=rentals.objects.get(id=pk)
#     rental.delete()
#     return Response({'message':'successfuly deleted'}) 
