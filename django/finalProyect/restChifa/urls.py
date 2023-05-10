from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dishes', views.dishes, name='dishes'),
    path('dish/<str:pk_name>', views.dish_detail, name='dish_detail'),
    path('menus', views.menus, name='menus'),
    path('menu/<str:pk_name>', views.menu_detail, name='menu_detail'),
    path('reserve', views.reserve, name='reserve'),
    path('contact', views.contact, name='contact'),
    path('data_reserves', views.data_reserves, name='data_reserves')
]