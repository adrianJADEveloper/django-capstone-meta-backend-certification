from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homeRestaurant(request):
    return HttpResponse('Hello World! from the Restaurant App!')
