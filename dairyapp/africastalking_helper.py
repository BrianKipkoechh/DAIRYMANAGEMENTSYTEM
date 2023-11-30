# africastalking_helper.py

import africastalking
from django.conf import settings

africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_sms(phone_number, message):
    try:
        response = sms.send(message, [phone_number])
        print(response)
    except Exception as e:
        print(f"Error sending SMS: {e}")
