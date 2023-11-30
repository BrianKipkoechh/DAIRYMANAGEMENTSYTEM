# api.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Delivery
from datetime import date

class DeliveryReminderAPI(APIView):
    def get(self, request, delivery_id):
        delivery = get_object_or_404(Delivery, pk=delivery_id)
        today = date.today()
        days_until_delivery = (delivery.delivery_date - today).days
        return Response({'days_until_delivery': days_until_delivery}, status=status.HTTP_200_OK)
