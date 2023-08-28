from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeRestaurant, name="homeRestaurant")
]
