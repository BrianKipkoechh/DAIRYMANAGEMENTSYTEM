from django import forms
from .models import Expense, MilkRecord, Delivery, cow, MilkingTime
from .models import cow

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['cow', 'expense_type', 'amount', 'date']

class MilkRecordForm(forms.ModelForm):
    class Meta:
        model = MilkRecord
        fields = ['cow', 'amount', 'date']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['cow', 'delivery_date']

class CowForm(forms.ModelForm):
        # name = forms.CharField(max_length=255, help_text="Enter the cow's name")
        class Meta:
            model =cow
            fields = '__all__'
class MilkingTimeForm(forms.ModelForm):
         class Meta:
            model = MilkingTime
            fields = ['milking_time']
