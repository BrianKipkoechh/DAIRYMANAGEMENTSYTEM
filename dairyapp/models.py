# models.py

from django.db import models

class cow(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    milk_production = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Expense(models.Model):
    cow = models.ForeignKey(cow, on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=255)
    amount = models.FloatField()
    date = models.DateField()

class MilkRecord(models.Model):
    cow = models.ForeignKey(cow, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()

class Delivery(models.Model):
    cow = models.ForeignKey(cow, on_delete=models.CASCADE)
    delivery_date = models.DateField()
class MilkingTime(models.Model):
    milking_time = models.TimeField()
