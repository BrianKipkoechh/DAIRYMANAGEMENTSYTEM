import code

from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from pyexpat.errors import messages
from .models import cow
from .forms import *
from .forms import CowForm
from .forms import MilkingTimeForm

from .africastalking_helper import send_sms
from .models import cow, Expense, MilkRecord, Delivery
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ExpenseForm, MilkRecordForm, DeliveryForm
def cow_list(request):
    cows = cow.objects.all()
    return render(request, 'cow_list.html', {'cows': cows})
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def milk_record_list(request):
    milk_records = MilkRecord.objects.all()
    return render(request, 'milk_record_list.html', {'milk_records': milk_records})

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery_form.html', {'deliveries': deliveries})

# ('dairyapp:delivery_list')# Expense views
class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_form.html'
    success_url = reverse_lazy('expense_list')

class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_form.html'
    success_url = reverse_lazy('expense_list')

class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'expense_confirm_delete.html'
    success_url = reverse_lazy('expense_list')

# MilkRecord views
class MilkRecordCreateView(CreateView):
    model = MilkRecord
    form_class = MilkRecordForm
    template_name = 'milk_record_form.html'
    success_url = reverse_lazy('milk_record_list')

class MilkRecordUpdateView(UpdateView):
    model = MilkRecord
    form_class = MilkRecordForm
    template_name = 'milk_record_form.html'
    success_url = reverse_lazy('milk_record_list')

class MilkRecordDeleteView(DeleteView):
    model = MilkRecord
    template_name = 'milk_record_confirm_delete.html'
    success_url = reverse_lazy('milk_record_list')

# Delivery views
class DeliveryCreateView(CreateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'delivery_form.html'
    success_url = reverse_lazy('delivery_list')

class DeliveryUpdateView(UpdateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'delivery_form.html'
    success_url = reverse_lazy('delivery_list')

class DeliveryDeleteView(DeleteView):
    model = Delivery
    template_name = 'delivery_confirm_delete.html'
    success_url = reverse_lazy
def home(request):
    return render(request, 'home.html')
def milking_time(request):
    milking_time_instance = MilkingTime.objects.first()  # Assuming there's only one milking time setting

    if request.method == 'POST':
        form = MilkingTimeForm(request.POST, instance=milking_time_instance)
        if form.is_valid():
            form.save()
            return redirect('milking_time_set_success')  # Redirect to a success page or any other URL
    else:
        form = MilkingTimeForm(instance=milking_time_instance)

    return render(request, 'milking_time_set.html', {'form': form})

def delivery_reminder(request):
    # Your delivery reminder logic here
    phone_number = "recipient_phone_number"
    message = "Reminder: Delivery is scheduled for the set time!"
    send_sms(phone_number, message)
    return render(request, 'delivery_reminder.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
class CowCreateView(CreateView):
    model = cow
    form_class = CowForm
    template_name = 'cow_form.html'
    success_url = reverse_lazy('cow_list')  # Update with your actual URL

class CowUpdateView(UpdateView):
    model = cow
    form_class = CowForm
    template_name = 'cow_form.html'
    success_url = reverse_lazy('cow_list')  # Update with your actual URL

class CowDeleteView(DeleteView):
    model = cow
    template_name = 'delete_cow.html'
    success_url = reverse_lazy('cow_list')  # Update with your actual URL
# Cow Form (forms.py):
# python
# Copy code
# dairyapp/forms.py

from django import forms
from .models import cow

class CowForm(forms.ModelForm):
    class Meta:
        model = cow
        fields = '__all__'
# Cow List View (views.py):
# python
# Copy code
# dairyapp/views.py

from django.shortcuts import render
from django.views.generic import ListView
from .models import cow


class SignupForm:
    pass


class CowListView(ListView):
    model = cow
    template_name = 'cow_list.html'
    context_object_name = 'cows'

def signup (request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                # Process the form data and create a new user
                # For simplicity, let's assume you have a User model
                # and you're using Django's built-in authentication system

                # Replace the following lines with your actual user creation logic
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                # Additional fields can be accessed similarly

                # Create a new user (this is a simplified example)
                # You might want to use Django's User.objects.create_user or a custom user model
                new_user = User.objects.create(username=username, password=password)

                # Log in the new user (optional)
                # login(request, new_user)

                # Redirect to a success page or login page
                return redirect('login')  # Replace 'login' with the actual name of your login page

        else:
            form = SignupForm()

        return render(request, 'signup.html', {'form': form})
def add_cow(request):
    if request.method == 'POST':
        form = CowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cow_list')  # Replace 'cow_list' with your cow list URL name
    else:
        form = CowForm()
    return render(request, 'cow_form.html', {'form': form})

def cow_form(request, cow_id):
    cow = get_object_or_404(cow, id=cow_id)
    if request.method == 'POST':
        form = CowForm(request.POST, instance=cow)
        if form.is_valid():
            form.save()
            return redirect('cow_list')  # Replace 'cow_list' with your cow list URL name
    else:
        form = CowForm(instance=cow)
    return render(request, 'cow_form.html', {'form': form, 'cow': cow})

def delete_cow(request, cow_id):
    cow = get_object_or_404(cow, id=cow_id)
    cow.delete()
    return redirect('cow_list.html')  # Replace 'cow_list' with your cow list URL name
def edit_cow(request, cow_id):
    cow = get_object_or_404(cow, id=cow_id)
    # Add your logic for editing cow details
    return render(request, 'edit_cow.html', {'cow': cow})
