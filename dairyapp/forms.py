from django import forms
from .models import Expense, MilkRecord, Delivery, Cow, MilkingTime
from .models import Cow
from django.views import View




class ExpenseForm(forms.Form):
  class Meta:
        model = Expense
        fields = ['description', 'amount']

class MilkRecordForm(forms.ModelForm):
    class Meta:
        model = MilkRecord
        fields = ['cow', 'amount', 'date']

   
class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['cow', 'delivery_date']
class AddCowForm(forms.Form):
    cow_name = forms.CharField(max_length=100, label='Cow Name')
    
class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ['name']
class MilkingTimeForm(forms.ModelForm):
         class Meta:
            model = MilkingTime
            fields = ['milking_time']
class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)