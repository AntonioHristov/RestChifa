from django.http import HttpResponse
from django.shortcuts import render

from .models import Restaurant, Reserve, Dish, Dish_menu, Contact, Contact_Phone, Contact_Mail



def menu(request):
    restaurant_objects = Restaurant.objects.all()
    context = {'restaurant_objects': restaurant_objects}
    return render(request, 'restChifa/menu.html', context)

def index(request):
    return HttpResponse("Hello, world.")