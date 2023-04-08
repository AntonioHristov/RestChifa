from django.contrib import admin

from .models import Restaurant, Reserve, Dish, Dish_menu, Contact, Contact_Phone, Contact_Mail





admin.site.register(Restaurant)
admin.site.register(Reserve)
admin.site.register(Dish)
admin.site.register(Dish_menu)
admin.site.register(Contact)
admin.site.register(Contact_Phone)
admin.site.register(Contact_Mail)