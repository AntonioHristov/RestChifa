from django.http import HttpResponse
from django.shortcuts import render

from .models import Restaurant, Reserve, Dish, Dish_menu, Contact, Contact_Phone, Contact_Mail



def index(request):
    dish_objects = Dish.objects.all()
    context = {
        'dish_objects': dish_objects
        }
    return render(request, 'restChifa/menu.html', context)

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

# ref: https://projectsplaza.com/how-to-save-form-data-in-database-in-django/
def reserve(request):
    restaurant_objects = Restaurant.objects.all()

    # FALTA VALIDAR QUE NO ESTE VACIO Y TAL
    if request.method=='POST' and request.POST:
        name=request.POST['name_reserve_name']
        phone=request.POST['name_reserve_tlf']
        date_utc=request.POST['name_reserve_date']


        for restaurant in restaurant_objects:
            if restaurant.name_restaurant == request.POST['name_reserve_restaurant']:
                name_restaurant=restaurant


        number_people=request.POST['name_reserve_people']
        email=request.POST['name_reserve_email']
        other=request.POST['name_reserve_other']
        


        reserve=Reserve.objects.create(name=name,phone=phone,date_utc=date_utc,name_restaurant=name_restaurant,number_people=number_people,email=email,other=other)


    context = {
    'restaurant_objects': restaurant_objects
    }

    return render(request,'restChifa/reserve.html', context)



def reservesssss(request):
    dish_objects = Dish.objects.all()
    context = {
        'dish_objects': dish_objects
        }
    return render(request, 'restChifa/reserve.html', context)

def contact(request):
    dish_objects = Dish.objects.all()
    context = {
        'dish_objects': dish_objects
        }
    return render(request, 'restChifa/contact.html', context)




