from django.contrib import admin

from .models import Restaurant, Reserve, Dish_type, Dish_category, Dish, Menu, Menu_Dish, Contact, Contact_Phone, Contact_Mail

class PK_Default_Admin(admin.ModelAdmin):
    search_fields = ['id']

class PK_Id_Admin(admin.ModelAdmin):
    search_fields = ['pk_id']

class PK_Name_Admin(admin.ModelAdmin):
    search_fields = ['pk_name']

class PK_MenuDish_Admin(admin.ModelAdmin):
    search_fields = ['fk_menu__pk_name', 'fk_dish__pk_name']

class PK_ContactPhone_Admin(admin.ModelAdmin):
    search_fields = ['fk_contact__pk_id', 'phone']

class PK_Contact_Mail_Admin(admin.ModelAdmin):
    search_fields = ['fk_contact__pk_id', 'email']
    




admin.site.register(Restaurant, PK_Name_Admin)
admin.site.register(Reserve, PK_Id_Admin)
admin.site.register(Dish_type, PK_Name_Admin)
admin.site.register(Dish_category, PK_Name_Admin)
admin.site.register(Dish, PK_Name_Admin)
admin.site.register(Menu, PK_Name_Admin)
admin.site.register(Menu_Dish, PK_MenuDish_Admin)
admin.site.register(Contact, PK_Id_Admin)
admin.site.register(Contact_Phone, PK_ContactPhone_Admin)
admin.site.register(Contact_Mail, PK_Contact_Mail_Admin)