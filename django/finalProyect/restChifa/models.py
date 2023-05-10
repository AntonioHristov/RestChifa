from django.db import models

from django.conf import settings
from .common import Common

# Create your models here.



class Restaurant(models.Model):
    pk_name = models.CharField(primary_key=True, max_length=200, blank = False, null = False)

    class Meta:
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.pk_name


class Reserve(models.Model):
    pk_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank = False, null = False)
    phone = models.CharField(max_length=15, blank = False, null = False)
    date_utc = models.DateTimeField('date reserve UTC')

    fk_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    number_people = models.IntegerField(default=1, blank = False, null = False)
    email = models.CharField(max_length=100, blank=True)
    other = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Reserves"

    def __str__(self):
        return 'ID: {}'.format(self.pk)

    def __is_valid_bool__(self):
        days_more = settings.DAYS_IN_ADVANCE_RESERVES
        seconds_more = settings.SECONDS_IN_ADVANCE_RESERVES
        return self.date_utc > Common.get_datetime_operation_add(timezone.now(),days_more,seconds_more)

    def __is_valid_this__(self):
        if __is_valid_bool__(self):
            return self


class Dish_type(models.Model):
    pk_name = models.CharField(primary_key=True, max_length=100, blank = False, null = False)

    class Meta:
        verbose_name_plural = "Dish_types"

    def __str__(self):
        return self.pk_name


class Dish_category(models.Model):
    pk_name = models.CharField(primary_key=True, max_length=100, blank = False, null = False)

    class Meta:
        verbose_name_plural = "Dish_categories"

    def __str__(self):
        return self.pk_name


class Dish(models.Model):
    pk_name = models.CharField(primary_key=True, max_length=200, blank = False, null = False)
    fk_type = models.ForeignKey(Dish_type, on_delete=models.CASCADE)
    fk_category = models.ForeignKey(Dish_category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank = False, null = False)
    description = models.CharField(max_length=200)
    src_photo = models.ImageField(default='no_image.jpg')
    popular = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.pk_name

class Menu(models.Model):
    pk_name = models.CharField(primary_key=True, max_length=200, blank = False, null = False)

    class Meta:
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.pk_name

class Menu_Dish(models.Model):
    fk_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    fk_dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Menu_Dishes"
        constraints = [
            models.UniqueConstraint(
                fields=['fk_menu', 'fk_dish'], name='unique_fk_menu_fk_dish_combination'
            )
        ]

    def __str__(self):
        return "Menu: " + self.fk_menu.pk_name + " | Plato: " + self.fk_dish.pk_name

class Contact(models.Model):
    pk_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank = False, null = False)
    main_phone = models.CharField(max_length=15, blank = False, null = False)
    main_email = models.CharField(max_length=100)
    other = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return "ID: " + str(self.pk_id) + " | Nombre: " + self.name

class Contact_Phone(models.Model):
    fk_contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank = False, null = False)
    phone = models.CharField(max_length=15, blank = False, null = False)

    class Meta:
        verbose_name_plural = "Contact_Phones"
        constraints = [
            models.UniqueConstraint(
                fields=['fk_contact', 'phone'], name='unique_fk_contact_phone_combination'
            )
        ]

    def __str__(self):
        return "ID Contact: " + str(self.fk_contact.pk_id) + " | Tlf Extra: " + self.phone

class Contact_Mail(models.Model):
    fk_contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank = False, null = False)
    email = models.CharField(max_length=100, blank = False, null = False)
    
    class Meta:
        verbose_name_plural = "Contact_Mails"
        constraints = [
            models.UniqueConstraint(
                fields=['fk_contact', 'email'], name='unique_fk_contact_email_combination'
            )
        ]

    def __str__(self):
        return "ID Contact: " + str(self.fk_contact.pk_id) + " | Email Extra: " + self.email

