from django.conf.urls import url, include
from .views import first_view,users,movies
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('users', users, basename='users')
router.register('movies', movies, basename='movies')


urlpatterns=[
    # url('first', first_view),
    # url('movie-list', movie_list),
    # url('rental-list', rental_list),
    # path('movie-detail/<str:pk>/', movie_detail),
    # path('rental-detail/<str:pk>/', rental_detail),
    # path('movie-create', movie_create),
    # path('create-rental', create_rental),
    # path('movie-update/<str:pk>/', movie_update),
    # path('update-rental/<str:pk>/', update_rental),
    # path('delete-rental/<str:pk>/', delete_rental),
    # path('movie-delete/<str:pk>/', movie_delete),
    url('', include(router.urls))
]