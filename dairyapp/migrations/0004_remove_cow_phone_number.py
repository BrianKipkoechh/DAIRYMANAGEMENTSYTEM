# Generated by Django 4.2.7 on 2023-12-01 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0003_cow_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cow',
            name='phone_number',
        ),
    ]
