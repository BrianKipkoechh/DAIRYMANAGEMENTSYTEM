# dairyapp/urls.py

from django.urls import path
from .views import *
from . import views, admin
from .views import home

app_name = 'dairyapp'

urlpatterns = [

    path('', views.home, name='home'),
    path('cows/', views.cow_list, name='cow_list'),
    path('expenses/',views. expense_list, name='expense_list'),
    path('milk records/', views.milk_record_list, name='milk_record_list'),
    path('deliveries/', views.delivery_list, name='delivery_list'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('add cow/',views.add_cow, name='add_cow'),
    path('cow form/<int:cow_id>/', views.cow_form, name='cow_form'),
    path('delete cow/<int:cow_id>/', views.delete_cow, name='delete_cow'),
    path('delivery reminder/', views.delivery_reminder, name='delivery_reminder'),
    path('edit cow/<int:cow_id>/', views.edit_cow, name='edit_cow'),
    path('set time/', views.milking_time, name='milking_time_set'),

]


