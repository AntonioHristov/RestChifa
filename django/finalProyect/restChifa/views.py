from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import get_current_timezone
import datetime
import pytz
from django.conf import settings


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


def reserve(request):
    restaurant_objects = Restaurant.objects.all()


    if request.method=='POST' and request.POST:
        name=request.POST['name_reserve_name']
        phone=request.POST['name_reserve_tlf']
        date_local=request.POST['name_reserve_date']

        # parse input datetime-local to object datetime format
        date_processing = date_local.replace('T', '-').replace(':', '-').split('-')
        date_processing = [int(v) for v in date_processing]
        date_local = datetime.datetime(*date_processing)




        
        #time_zone = pytz.timezone(timezone.get_current_timezone_name())
        #time_zone = pytz.timezone('Europe/Madrid')
        time_zone = pytz.timezone(settings.TIME_ZONE_USER)


        date_time = date_local
        # make time zone aware
        date_local = time_zone.localize(date_time)

        # convert to UTC
        date_utc = date_local.astimezone(pytz.utc)










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


def contact(request):
    dish_objects = Dish.objects.all()
    context = {
        'dish_objects': dish_objects
        }
    return render(request, 'restChifa/contact.html', context)



def data_reserves(request):
    restaurant_objects = Restaurant.objects.all()
    reserve_objects = Reserve.objects.all()
    dish_objects = Dish.objects.all()
    dish_types = Dish.objects.values_list('name_type', flat=True).distinct().all()

    context = {
        'restaurant_objects': restaurant_objects,
        'reserve_objects': reserve_objects,
        'dish_types': dish_types,
        'dish_types': dish_types
        }
    return render(request, 'restChifa/data_reserves.html', context)
