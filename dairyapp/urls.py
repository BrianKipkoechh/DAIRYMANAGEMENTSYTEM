# dairyapp/urls.py

from django.urls import path
from .views import *
from . import views, admin
from .views import home
from .views import MilkRecordCreateView,MilkRecordListView
from .views import DeleteView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import CowListView
from .views import MilkRecordForm
# app_name = 'dairyapp'

urlpatterns = [

    path('', views.home, name='home'),
    path('cows/', views.cow_list, name='cow_list'),
    path('expenses/',views. expense_list, name='expense_list'),
    path('milk_records/', views.milk_record_list, name='milk_record_list'),
    path('deliveries/', views.delivery_list, name='delivery_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('add_cow/',views.add_cow, name='add_cow'),
    path('cow_form/<int:cow_id>/', views.CowForm, name='cow_form'),
    path('milk-record/list/', MilkRecordListView.as_view(), name='milk_record_list'),
    path('delete_cow/<int:cow_id>/', delete_cow, name='delete_cow'),
    path('edit_cow/<int:cow_id>/', CowUpdateView.as_view, name='edit_cow'),
    path('set_time/', views.milking_time, name='milking_time_set'),
    path('milk_record/create/', MilkRecordCreateView.as_view(), name='milk_record/create'),
    path('expense/create/', ExpenseCreateView.as_view(), name='expense_create'),
    path('delivery/create/', DeliveryCreateView.as_view(), name='delivery_create'),
    path('milking_time/set/', MilkingTimeCreateView.as_view(), name='milking_time_set'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('expense_form/', views.expense_form, name='expense_form'),
    path('cow-list/', CowListView.as_view(), name='cow_list'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('milk-record/form/', MilkRecordForm.as_view(), name='milk_record_form'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

