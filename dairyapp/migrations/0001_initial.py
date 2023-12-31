# Generated by Django 4.2.7 on 2023-12-01 21:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pregnancy_status', models.CharField(max_length=50)),
                ('last_service_date', models.DateField(default=datetime.date(2023, 12, 2))),
                ('expected_delivery_date', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MilkingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milking_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MilkRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('cow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairyapp.cow')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_type', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('cow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairyapp.cow')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField()),
                ('cow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairyapp.cow')),
            ],
        ),
    ]
