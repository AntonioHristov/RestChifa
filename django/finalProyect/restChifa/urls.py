from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dishes', views.dishes, name='dishes'),
    path('reserve', views.reserve, name='reserve'),
    path('contact', views.contact, name='contact')
]