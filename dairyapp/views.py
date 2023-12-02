import code
from urllib import request

from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from pyexpat.errors import messages

from django.views import View
from .models import Cow
from .forms import *
from django.urls import reverse
from .forms import CowForm
from .forms import MilkingTimeForm
from django.shortcuts import render
from django.views.generic import ListView
from .forms import ExpenseForm

from .forms import SignupForm

from .models import Cow, Expense, MilkRecord, Delivery, MilkingTime
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ExpenseForm, MilkRecordForm, DeliveryForm, MilkingTimeForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the home page after successful signup
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
def cow_list(request):
    cows = Cow.objects.all()
    success_message = messages.get_messages(request).first()
    return render(request, 'cow_list.html', {'cows': cows})

def expense_form(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            # Redirect to a success page or any other URL
            return redirect('expense_list')  # Replace with your actual URL
    else:
        form = ExpenseForm()

    return render(request, 'expense_form.html', {'form': form})
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})
def add_cow(request):
    if request.method == 'POST':
        form = CowForm(request.POST)
        if form.is_valid():
            cows = Cow.objects.all()
            cow = form.save()
            
            return redirect('cow_list')  # Replace 'cow_list' with your actual URL name for the cow list view
            
            
           
    else:
        form = CowForm()
    return render(request, 'add_cow.html', {'form': form})

def milk_record_create(request):
    if request.method == 'POST':
        form = MilkRecordForm(request.POST)
        if form.is_valid():
            milk_records = MilkRecord.objects.all()
            form.save()
            return redirect('milk_record_list')
    else:
        form = MilkRecordForm()

    return render(request, 'milk_record_create.html', {'form': form})

def milk_record_list(request):
    milk_records = MilkRecord.objects.all()
    return render(request, 'milk_record_list.html', {'milk_records': milk_records})


def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery_form.html', {'deliveries': deliveries})


# MilkingTime views
class MilkingTimeCreateView(CreateView):
    model = MilkingTime
    form_class = MilkingTimeForm
    template_name = 'milking_time_form.html'  # Adjust this to match your actual template
    success_url = reverse_lazy('milking_time_list')  # Adjust this to match your actual URL name


class MilkingTimeUpdateView(UpdateView):
    model = MilkingTime
    form_class = MilkingTimeForm
    template_name = 'milking_time_form.html'  # Adjust this to match your actual template
    success_url = reverse_lazy('milking_time_list')  # Adjust this to match your actual URL name


class MilkingTimeDeleteView(DeleteView):
    model = MilkingTime
    template_name = 'milking_time_confirm_delete.html'  # Adjust this to match your actual template


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



class LoginView(View):
    model = MilkRecord
    template_name = 'login.html'
    success_url = reverse_lazy('login')
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the desired page after successful login
            return redirect('home')  # Replace 'home' with your actual home page URL name
        else:
            # Handle invalid login
            return render(request, self.template_name, {'error_message': 'Invalid username or password'})


class CowCreateView(CreateView):
    model = Cow
    form_class = CowForm
    template_name = 'cow_form.html'
    success_url = reverse_lazy('cow_list')  # Update with your actual URL


class CowUpdateView(UpdateView):
    model = Cow
    form_class = CowForm
    template_name = 'cow_form.html'
    success_url = reverse_lazy('cow_list')  # Update with your actual URL


class CowDeleteView(DeleteView):
    model = Cow
    template_name = 'delete_cow.html'
    success_url = reverse_lazy('cow_list')  # Update with your actual URL
def get_queryset(self):
        return Cow.objects.all()

# Cow Form (forms.py):
# python
# Copy code
# dairyapp/forms.py

from django import forms
from .models import Cow


class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = '__all__'


# Cow List View (views.py):
# python
# Copy code
# dairyapp/views.py





class CowListView(View):
    def get(self, request):
        # Your existing logic to get the list of cows
        cows = Cow.objects.all()

        # Example of reversing the delete_cow URL
        delete_cow_url = reverse('delete_cow', args=[1])  # Replace 1 with the actual cow_id

        return render(request, 'cow_list.html', {'cows': cows, 'delete_cow': delete_cow})


class SignupView(CreateView):
    template_name = 'signup.html'  # Replace with your actual template name
    new_tepmlate='home.html'
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        return render(request, self.new_tepmlate, {'form': form})
class LoginView(View):
    template_name = 'login.html'
    success_url = '/home/'  # Replace with your desired success URL

    def get(self, request, *args, **kwargs):
        form = LoginForm()  # Create an instance of the LoginForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)  # Bind the form with POST data

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(self.success_url)
            else:
                form.add_error(None, 'Invalid credentials')
        
        # If form is invalid or authentication fails, render the login page with the form and errors
                return render(request, self.template_name, {'form': form})
def delete_cow(request, cow_id):
    Cow = Cow.objects.get(id=cow_id)
    Cow.delete()
    return redirect('cow_list')
def add_milk_record(request):
    if request.method == 'POST':
        form = MilkRecordForm(request.POST)
        if form.is_valid():
            milk_records = MilkRecord.objects.all()
            form.save()
            return redirect('milk_record_list')  # Replace 'milk_record_list' with your actual URL name for the milk record list view
    else:
        form = MilkRecordForm()

    return render(request, 'milk_record_list.html', {'form': form})