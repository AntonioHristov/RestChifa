from django.http import HttpResponse
from django.shortcuts import render

from .models import Restaurant, Reserve, Dish, Dish_menu, Contact, Contact_Phone, Contact_Mail



def dishes(request):
    restaurant_objects = Restaurant.objects.all()
    dish_objects = Dish.objects.all()
    dish_types = Dish.objects.values_list('name_type', flat=True).distinct().all()
    context = {
        'restaurant_objects': restaurant_objects,
        'dish_objects': dish_objects,
        'dish_types': dish_types
        }
    return render(request, 'restChifa/dishes.html', context)

def index(request):
    restaurant_objects = Restaurant.objects.all()
    dish_objects = Dish.objects.all()
    dish_types = Dish.objects.values_list('name_type', flat=True).distinct().all()
    context = {
        'restaurant_objects': restaurant_objects,
        'dish_objects': dish_objects,
        'dish_types': dish_types
        }
    return render(request, 'restChifa/menu.html', context)