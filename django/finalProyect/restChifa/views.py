from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import get_current_timezone
import datetime
import pytz
from django.conf import settings


from .models import Restaurant, Reserve, Dish, Dish_menu, Contact, Contact_Phone, Contact_Mail
from .common import get_datetime_operation_add


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

    success = ""
    errorname = ""
    errortlf = ""
    errordate = ""
    errorrestaurant = ""
    errorpeople = ""
    erroremail = ""
    errorother = ""

    if request.method=='POST' and request.POST:
        name=request.POST['name_reserve_name']
        phone=request.POST['name_reserve_tlf']
        date_local=request.POST['name_reserve_date']


        try:
            bool(datetime.datetime.strptime(date_local, "%Y-%m-%dT%H:%M"))
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
        except ValueError:
            date_utc = ""

          

        name_restaurant = ""
        for restaurant in restaurant_objects:
            if restaurant.name_restaurant == request.POST['name_reserve_restaurant']:
                name_restaurant=restaurant

        number_people=request.POST['name_reserve_people']
        email=request.POST['name_reserve_email']
        other=request.POST['name_reserve_other']
        


        if name == "" or name.isspace() :
            errorname = "El nombre no debe estar vacío"

        if phone == "" or phone.isspace() or not phone.isnumeric() :
            errortlf = "El teléfono no debe estar vacío y debe ser un número entero no negativo"

        if date_utc == "" or date_utc < get_datetime_operation_add(timezone.now(), settings.DAYS_IN_ADVANCE_RESERVES, settings.SECONDS_IN_ADVANCE_RESERVES) :
            errordate = "Elige una fecha válida, debe haber al menos 1 hora de diferencia"

        if name_restaurant == "" :
            errorrestaurant = "Debes elegir un restaurante, haz click en el desplegable y elige uno"

        if not number_people.isnumeric() or "," in number_people or "." in number_people or int(number_people) < 1 :
            errorpeople = "Debe ser un número entero mayor a 0... ¿Que demonios, intentas romper mi sitio web?"



        if errorname == "" and errortlf == "" and errordate == "" and errorrestaurant == "" and errorpeople == "" and erroremail == "" and errorother == "" :
            reserve = Reserve.objects.create(name=name,phone=phone,date_utc=date_utc,name_restaurant=name_restaurant,number_people=number_people,email=email,other=other)
            success = "Su reserva ha sido realizada con éxito. Guarda tu Identificador, es: " + str(reserve.pk)



    error = {
    'name': errorname,
    'tlf': errortlf,
    'date': errordate,
    'restaurant': errorrestaurant,
    'people': errorpeople
    }

    post = {
    'name_reserve_name': request.POST.get("name_reserve_name", ""),
    'name_reserve_tlf': request.POST.get("name_reserve_tlf", ""),
    'name_reserve_date': request.POST.get("name_reserve_date", ""),
    'name_reserve_restaurant': request.POST.get("name_reserve_restaurant", ""),
    'name_reserve_people': request.POST.get("name_reserve_people", 1),
    'name_reserve_email': request.POST.get("name_reserve_email", ""),
    'name_reserve_other': request.POST.get("name_reserve_other", ""),
    'success': success,
    'error': error
    }
        
    context = {
    'restaurant_objects': restaurant_objects,
    'post': post
    }

    return render(request,'restChifa/reserve.html', context)


def contact(request):
    contact_objects = Contact.objects.all()
    context = {
        'contact_objects': contact_objects
        }
    return render(request, 'restChifa/contact.html', context)



def data_reserves(request):
    reserve_objects = Reserve.objects.all()
    user_timezone = settings.TIME_ZONE_USER


    context = {
        'reserve_objects': reserve_objects,
        'user_timezone': user_timezone
        }
    return render(request, 'restChifa/data_reserves.html', context)

