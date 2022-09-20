from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import os
import binascii

def send__email(email_data):
    # Verified will be the initial state of the booking before updating is done
    if(email_data['initial_verified_status'] == False and email_data['new_verified_status'] == True):
        print("Sending verification email")
        if(email_data['send_verification_email'] == True):
            print(email_data['send_verification_email'])

            context = {
                'name': email_data['customer_name'],
                'email': email_data['customer_email'],
                'booking_type': email_data['booking_type'],
                'court_location': email_data['court_location'],
                'start_date': email_data['start_date'],
                'end_date': email_data['end_date'],
                'start_time': email_data['start_time'],
                'end_time': email_data['end_time'],
                'cost': email_data['cost'],
                'duration': email_data['duration'],
                'verified_by': email_data['verified_by']
            }
            # print(context)
            email_subject = 'Your booking has been verified'
            html_content = render_to_string('email_message.txt', context)

            email = EmailMessage(
                email_subject, html_content,
                settings.DEFAULT_FROM_EMAIL, [email_data['customer_email'], ],
            )
            email.content_subtype = "html"
            email.send(fail_silently=False)
        else:
            pass
    else:
        pass

