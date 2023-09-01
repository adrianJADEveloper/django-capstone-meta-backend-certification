from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User # for the User
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .models import Menu, Booking

from rest_framework import viewsets

# Create your views here.


def homeRestaurant(request):
    return HttpResponse('Hello World! from the Restaurant App!')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# class UserView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class BookingView(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

# class BookingSingleView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

