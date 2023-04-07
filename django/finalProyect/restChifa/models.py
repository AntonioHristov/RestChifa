from django.db import models

# Create your models here.



class Restaurant(models.Model):
    name_restaurant = models.CharField(primary_key=True, max_length=200, blank = False, null = False)

    def __str__(self):
        return self.name_restaurant

class Reserve(models.Model):
    # id_reserve = models.IntegerField(primary_key=True, default=0, auto_now_add=True)
    name = models.CharField(max_length=200, blank = False, null = False)
    phone = models.CharField(max_length=15, blank = False, null = False)

    # date_utc = models.DateTimeField(blank = False, null = False)

    # name_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank = False, null = False)
    name_restaurant = models.CharField(max_length=200, blank = False, null = False)
    # number_people = models.IntegerField(default=0, blank = False, null = False)
    email = models.CharField(max_length=100)
    other = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def is_valid(self):
        return self.date_utc >= timezone.now() - datetime.timedelta(hours=1)


class Dish(models.Model):
    name_dish = models.CharField(primary_key=True, max_length=200, blank = False, null = False)
    name_type = models.CharField(max_length=100, blank = False, null = False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank = False, null = False)
    description = models.CharField(max_length=200)
    src_photo = models.ImageField(default='no_image.jpg')
    popular = models.IntegerField(default=0)

    def __str__(self):
        return self.name_dish

class Dish_menu(models.Model):
    name_dish = models.ForeignKey(Dish, on_delete=models.CASCADE, blank = False, null = False)
    name_menu = models.CharField(max_length=200, blank = False, null = False)

    def __str__(self):
        return self.name_menu

class Contact(models.Model):
    name = models.CharField(max_length=200, blank = False, null = False)
    main_phone = models.CharField(max_length=15, blank = False, null = False)
    main_email = models.CharField(max_length=100)
    other = models.CharField(max_length=200)

    def __str__(self):
        return self.name

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

