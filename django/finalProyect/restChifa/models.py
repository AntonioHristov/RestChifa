from django.db import models

from django.conf import settings
from .common import get_datetime_operation_add

# Create your models here.



class Restaurant(models.Model):
    name_restaurant = models.CharField(primary_key=True, max_length=200, blank = False, null = False)

    def __str__(self):
        return self.name_restaurant



class Reserve(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank = False, null = False)
    phone = models.CharField(max_length=15, blank = False, null = False)
    date_utc = models.DateTimeField('date reserve UTC')

    name_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    number_people = models.IntegerField(default=1, blank = False, null = False)
    email = models.CharField(max_length=100, blank=True)
    other = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return 'ID: {}'.format(self.pk)

    def __is_valid__(self):
        days_more = settings.DAYS_IN_ADVANCE_RESERVES
        seconds_more = settings.SECONDS_IN_ADVANCE_RESERVES
        return self.date_utc > get_datetime_operation_add(timezone.now(),days_more,seconds_more)




class Dish(models.Model):
    name_dish = models.CharField(primary_key=True, max_length=200, blank = False, null = False)
    type = models.CharField(max_length=100, blank = False, null = False)
    category = models.CharField(max_length=100)#, blank = False, null = False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank = False, null = False)
    description = models.CharField(max_length=200)
    src_photo = models.ImageField(default='no_image.jpg')
    popular = models.IntegerField(default=0)

    def __str__(self):
        return self.name_dish

class Menu(models.Model):
    name = models.CharField(primary_key=True, max_length=200, blank = False, null = False)

    def __str__(self):
        return self.name

class Menu_Dish(models.Model):
    name_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name_dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return "Menu: " + self.name_menu.name + " | Plato: " + self.name_dish.name_dish

class Contact(models.Model):
    name = models.CharField(max_length=200, blank = False, null = False)
    main_phone = models.CharField(max_length=15, blank = False, null = False)
    main_email = models.CharField(max_length=100)
    other = models.CharField(max_length=200)

    def __str__(self):
        return 'ID: {}'.format(self.pk)

class Contact_Phone(models.Model):
    id_contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank = False, null = False)
    number_phone = models.CharField(max_length=15, blank = False, null = False)

    def __str__(self):
        return self.number_phone

class Contact_Mail(models.Model):
    id_contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank = False, null = False)
    email = models.CharField(max_length=100, blank = False, null = False)

    def __str__(self):
        return self.email

