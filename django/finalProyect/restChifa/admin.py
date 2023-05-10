from django.contrib import admin

from .models import Restaurant, Reserve, Dish_type, Dish_category, Dish, Menu, Menu_Dish, Contact, Contact_Phone, Contact_Mail

class PK_Default_Admin(admin.ModelAdmin):
    search_fields = ['id']




admin.site.register(Restaurant)
admin.site.register(Reserve, PK_Default_Admin)
admin.site.register(Dish_type)
admin.site.register(Dish_category)
admin.site.register(Dish)
admin.site.register(Menu)
admin.site.register(Menu_Dish)
admin.site.register(Contact, PK_Default_Admin)
admin.site.register(Contact_Phone)
admin.site.register(Contact_Mail)