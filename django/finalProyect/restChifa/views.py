from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import get_current_timezone
import datetime
import pytz
from django.conf import settings
from django.views.generic import ListView
import re
from django.db.models import Q
from .common import Common


from .models import Restaurant, Reserve, Dish_type, Dish_category, Dish, Menu, Menu_Dish, Contact, Contact_Phone, Contact_Mail


def index(request):
    search_get = request.GET.get('search')
    dish_objects = Dish.objects.all().order_by('-popular', 'pk_name')

    if search_get:
        dish_objects = dish_objects.filter(Q(pk_name__icontains=search_get))

    page_object = Common.get_paginator(request, dish_objects)
    nav_index_active = "active"

    url_page = {
        "index": settings.URL_INDEX,
        "dishes": settings.URL_DISHES,
        "dish": settings.URL_DISH,
        "menus": settings.URL_MENUS,
        "menu": settings.URL_MENU,
        "reserve": settings.URL_RESERVE,
        "contact": settings.URL_CONTACT,
        "data_reserves": settings.URL_DATA_RESERVES
    }

    context = {
        "page_object": page_object,
        "nav_index_active": nav_index_active,
        "url_page": url_page
        }
    return render(request, 'restChifa/index.html', context)

def dishes(request):
    search_get = request.GET.get('search')
    dish_objects = Dish.objects.all().order_by('-popular', 'pk_name')

    if search_get:
        dish_objects = dish_objects.filter(Q(pk_name__icontains=search_get))

    #dish_objects = Dish.objects.all().order_by('-popular', 'pk_name')

    try:
        dish_fk_objects = dish_objects.values('fk_category__pk_name', 'fk_type__pk_name').distinct().order_by('fk_category__position').all()
    except Dish.DoesNotExist:
        dish_fk_objects = False

    try:
        page_object = Common.get_paginator(request, dish_objects.values('fk_type__pk_name').distinct().order_by('fk_type__position').all(), 1)
    except Dish.DoesNotExist:
        page_object = False

    
    nav_dishes_active = "active"

    url_page = {
        "index": settings.URL_INDEX,
        "dishes": settings.URL_DISHES,
        "dish": settings.URL_DISH,
        "menus": settings.URL_MENUS,
        "menu": settings.URL_MENU,
        "reserve": settings.URL_RESERVE,
        "contact": settings.URL_CONTACT,
        "data_reserves": settings.URL_DATA_RESERVES
    }

    context = {
        'dish_fk_objects': dish_fk_objects,
        'dish_objects': dish_objects,
        'page_object': page_object,
        "nav_dishes_active": nav_dishes_active,
        "url_page": url_page
        }
        
    return render(request, 'restChifa/dishes.html', context)


def dish_detail(request, pk_name):
    try:
        dish = Dish.objects.get(pk__iexact=pk_name)
    except Dish.DoesNotExist:
        dish = False

    nav_dishes_active = "active"

    url_page = {
        "index": settings.URL_INDEX,
        "dishes": settings.URL_DISHES,
        "dish": settings.URL_DISH,
        "menus": settings.URL_MENUS,
        "menu": settings.URL_MENU,
        "reserve": settings.URL_RESERVE,
        "contact": settings.URL_CONTACT,
        "data_reserves": settings.URL_DATA_RESERVES
    }

    context = {
    'dish': dish,
    "nav_dishes_active": nav_dishes_active,
    "url_page": url_page
    }
    return render(request, 'restChifa/dish_detail.html', context)


def menus(request):
    search_get = request.GET.get('search')
    menu_objects = Menu.objects.all()

    if search_get:
        menu_objects = menu_objects.filter(Q(pk_name__icontains=search_get))

    page_object = Common.get_paginator(request, menu_objects)
    nav_menus_active = "active"
    url_page = {
        "index": settings.URL_INDEX,
        "dishes": settings.URL_DISHES,
        "dish": settings.URL_DISH,
        "menus": settings.URL_MENUS,
        "menu": settings.URL_MENU,
        "reserve": settings.URL_RESERVE,
        "contact": settings.URL_CONTACT,
        "data_reserves": settings.URL_DATA_RESERVES
    }

    context = {
        'page_object': page_object,
        "nav_menus_active": nav_menus_active,
        "url_page": url_page
        }
    return render(request, 'restChifa/menus.html', context)


def menu_detail(request, pk_name):
    search_get = request.GET.get('search')
    try:
        menu_objects = Menu.objects.get(pk__iexact=pk_name)
    except Menu.DoesNotExist:
        menu_objects = False

    try:
        menu_dish_objects = Menu_Dish.objects.filter(fk_menu=pk_name)
        if search_get:
            menu_dish_objects = menu_dish_objects.filter(Q(fk_dish__pk_name__icontains=search_get))
    except Menu_Dish.DoesNotExist:
        menu_dish_objects = False

    try:
        menu_dish_fk_objects = menu_dish_objects.values('fk_dish__fk_category__pk_name', 'fk_dish__fk_type__pk_name').distinct().order_by('fk_dish__fk_category__position').all()
    except Menu_Dish.DoesNotExist:
        menu_dish_fk_objects = False

    try:
        page_object = Common.get_paginator(request, menu_dish_objects.values('fk_dish__fk_type__pk_name').distinct().order_by('fk_dish__fk_type__position').all(), 1)
    except Menu_Dish.DoesNotExist:
        page_object = False



    
    nav_menus_active = "active"
    url_page = {
        "index": settings.URL_INDEX,
        "dishes": settings.URL_DISHES,
        "dish": settings.URL_DISH,
        "menus": settings.URL_MENUS,
        "menu": settings.URL_MENU,
        "reserve": settings.URL_RESERVE,
        "contact": settings.URL_CONTACT,
        "data_reserves": settings.URL_DATA_RESERVES
    }

    context = {
        'menu_objects': menu_objects, 
        'menu_dish_objects': menu_dish_objects,
        'menu_dish_fk_objects': menu_dish_fk_objects,
        'page_object': page_object,
        "nav_menus_active": nav_menus_active,
        "url_page": url_page
        }

    return render(request, 'restChifa/menu_detail.html', context)


def reserve(request):
    restaurant_objects = Restaurant.objects.all()
    nav_reserve_active = "active"

    success = ""
    errorname = ""
    errorprefixtlf = ""
    errortlf = ""
    errordate = ""
    errorrestaurant = ""
    errorpeople = ""
    erroremail = ""
    errorother = ""

    if request.method=='POST' and request.POST:
        name=request.POST['name_reserve_name']
        prefix_phone=request.POST['name_reserve_prefix_tlf'] 
        validate_prefix_phone_pattern = "^\\+?[1-9]{1,2}([0-9]?|\\-?){0,5}$"
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
            if restaurant.pk_name == request.POST['name_reserve_restaurant']:
                name_restaurant=restaurant

        number_people=request.POST['name_reserve_people']
        email=request.POST['name_reserve_email']
        other=request.POST['name_reserve_other']
        


        if name == "" or name.isspace() :
            errorname = "El nombre no debe estar vacío"
        elif len(name) > 200 :
            errorname = "El nombre no debe tener más de 200 caracteres"

        if not re.match(validate_prefix_phone_pattern, prefix_phone) :
            errorprefixtlf = "El prefijo no es válido, [contenido] = opcional. El formato es: [+](Número del 1 al 9)[(Número del 0 al 9 o carácter -)] (Los caracteres totales deben ser entre 1 y 7)"
        elif phone == "" or phone.isspace() or not phone.isnumeric() :
            errortlf = "El teléfono no debe estar vacío y debe ser un número entero no negativo"
        elif len(phone) < 9 :
            errortlf = "El teléfono no debe tener menos de 9 caracteres"
        elif len(phone) > 14 :
            errortlf = "El teléfono no debe tener más de 14 caracteres"
        else :
            phone = str(prefix_phone) + " " + str(phone)

        if date_utc == "" or not Common.is_valid_date_reserve(date_utc) :
            errordate = "Elige una fecha válida, debe haber al menos 1 hora de diferencia"

        if name_restaurant == "" :
            errorrestaurant = "Debes elegir un restaurante, haz click en el desplegable y elige uno"

        if not number_people.isnumeric() or "," in number_people or "." in number_people or int(number_people) < 1 or int(number_people) > settings.MAXIMUM_PEOPLE_PER_RESERVE :
            errorpeople = "Debe ser un número entero mayor a 0 y menor a " + str(settings.MAXIMUM_PEOPLE_PER_RESERVE + 1)

        if len(email) > 100 :
            erroremail = "El email no debe tener más de 100 caracteres"

        if len(other) > 200 :
            errorother = "Los datos extra no deben tener más de 200 caracteres"


        if errorname == "" and errorprefixtlf == "" and errortlf == "" and errordate == "" and errorrestaurant == "" and errorpeople == "" and erroremail == "" and errorother == "" :
            reserve = Reserve.objects.create(name=name,phone=phone,date_utc=date_utc,fk_restaurant=name_restaurant,number_people=number_people,email=email,other=other)
            success = "Su reserva ha sido realizada con éxito. Guarda tu Identificador, es: " + str(reserve.pk)


    add_class_is_invalid = {
    'name': "is-invalid" if errorname != "" else "",
    'prefix_tlf': "is-invalid" if errorprefixtlf != "" else "",
    'tlf': "is-invalid" if errortlf != "" else "",
    'date': "is-invalid" if errordate != "" else "",
    'restaurant': "is-invalid" if errorrestaurant != "" else "",
    'people': "is-invalid" if errorpeople != "" else "",
    'email': "is-invalid" if erroremail != "" else "",
    'other': "is-invalid" if errorother != "" else ""
    }

    error = {
    'name': errorname,
    'prefix_tlf': errorprefixtlf,
    'tlf': errortlf,
    'date': errordate,
    'restaurant': errorrestaurant,
    'people': errorpeople,
    'email': erroremail,
    'other': errorother,
    'add_class_is_invalid': add_class_is_invalid
    }

    post = {
    'name_reserve_name': request.POST.get("name_reserve_name", ""),
    'name_reserve_prefix_tlf': request.POST.get("name_reserve_prefix_tlf", ""),
    'name_reserve_tlf': request.POST.get("name_reserve_tlf", ""),
    'name_reserve_date': request.POST.get("name_reserve_date", ""),
    'name_reserve_restaurant': request.POST.get("name_reserve_restaurant", ""),
    'name_reserve_people': request.POST.get("name_reserve_people", 1),
    'name_reserve_email': request.POST.get("name_reserve_email", ""),
    'name_reserve_other': request.POST.get("name_reserve_other", ""),
    'success': success,
    'error': error
    }
        
    url_page = {
        "index": settings.URL_INDEX,
        "dishes": settings.URL_DISHES,
        "dish": settings.URL_DISH,
        "menus": settings.URL_MENUS,
        "menu": settings.URL_MENU,
        "reserve": settings.URL_RESERVE,
        "contact": settings.URL_CONTACT,
        "data_reserves": settings.URL_DATA_RESERVES
    }

    context = {
        'restaurant_objects': restaurant_objects,
        'post': post,
        "nav_reserve_active": nav_reserve_active,
        "url_page": url_page
    }

    return render(request,'restChifa/reserve.html', context)


def contact(request):
    search_get = request.GET.get('search')
    contact_objects = Contact.objects.all()
    phone_objects = Contact_Phone.objects.all()
    mail_objects = Contact_Mail.objects.all()

    if search_get:
        contact_objects = contact_objects.filter(Q(pk_id__icontains=search_get) | Q(name__icontains=search_get) | Q(main_phone__icontains=search_get) | Q(main_email__icontains=search_get))
        phone_objects = phone_objects.filter(Q(phone__icontains=search_get))
        mail_objects = mail_objects.filter(Q(email__icontains=search_get))


    page_object = Common.get_paginator(request, contact_objects, 1)

    nav_contact_active = "active"

    url_page = {
        "index": settings.URL_INDEX,
        "dishes": settings.URL_DISHES,
        "dish": settings.URL_DISH,
        "menus": settings.URL_MENUS,
        "menu": settings.URL_MENU,
        "reserve": settings.URL_RESERVE,
        "contact": settings.URL_CONTACT,
        "data_reserves": settings.URL_DATA_RESERVES
    }

    context = {
        'page_object': page_object,
        'phone_objects': phone_objects,
        'mail_objects': mail_objects,
        "nav_contact_active": nav_contact_active,
        "url_page": url_page
        }
    return render(request, 'restChifa/contact.html', context)



def data_reserves(request):
    #page_object = Common.get_paginator(request, Reserve.objects.all().order_by('date_utc'), 1)
    page_object = Common.get_paginator(request, Reserve.objects.filter(date_utc__gte = timezone.now()).order_by('date_utc'), 1)
    user_timezone = settings.TIME_ZONE_USER
    nav_data_reserves_active = "active"
    url_page = {
        "index": settings.URL_INDEX,
        "dishes": settings.URL_DISHES,
        "dish": settings.URL_DISH,
        "menus": settings.URL_MENUS,
        "menu": settings.URL_MENU,
        "reserve": settings.URL_RESERVE,
        "contact": settings.URL_CONTACT,
        "data_reserves": settings.URL_DATA_RESERVES
    }

    context = {
        'page_object': page_object,
        'user_timezone': user_timezone,
        "nav_data_reserves_active": nav_data_reserves_active,
        "url_page": url_page
        }
    return render(request, 'restChifa/data_reserves.html', context)


class DishListView(ListView):
    paginate_by = 1
    model = Dish