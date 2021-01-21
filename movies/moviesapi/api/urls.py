from django.conf.urls import url, include
from .views import first_view,users,movies,movie_rentals
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('users', users, basename='users')
router.register('movies', movies, basename='movies')
router.register('rentals', movie_rentals, basename='rentals')


urlpatterns=[
    
    url('', include(router.urls))
]