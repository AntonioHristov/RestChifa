from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path(settings.URL_INDEX, views.index, name='index'),
    path(settings.URL_DISHES, views.dishes, name='dishes'),
    path(settings.URL_DISH + '<str:pk_name>', views.dish_detail, name='dish_detail'),
    path(settings.URL_MENUS, views.menus, name='menus'),
    path(settings.URL_MENU + '<str:pk_name>', views.menu_detail, name='menu_detail'),
    path(settings.URL_RESERVE, views.reserve, name='reserve'),
    path(settings.URL_CONTACT, views.contact, name='contact'),
    path(settings.URL_DATA_RESERVES, views.data_reserves, name='data_reserves'),
    path(settings.URL_DATA_RESERVES + '<str:pk_name>', views.data_reserves_detail, name='data_reserves_detail')
]