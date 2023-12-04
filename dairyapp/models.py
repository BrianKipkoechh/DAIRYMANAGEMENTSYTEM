# models.py

from django.db import models
from datetime import date

class Cow(models.Model):
    name = models.CharField(max_length=100)
   
    

    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
class MilkRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    def __str__(self):
        return f"{self.cow.name} - {self.amount} liters on {self.date}"

class Delivery(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    delivery_date = models.DateField()

class MilkingTime(models.Model):
    milking_time = models.TimeField()
