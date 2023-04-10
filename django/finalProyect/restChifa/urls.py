from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dishes', views.dishes, name='dishes'),
    path('reserve', views.reserve, name='reserve'),
    path('contact', views.contact, name='contact'),
    path('data_reserves', views.data_reserves, name='data_reserves')
]