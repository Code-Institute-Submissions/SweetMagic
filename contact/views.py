from django.shortcuts import (redirect, reverse)
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def contact_request(request):
    recipient_email = "orders.sweetmagic@gmail.com"
    sender_email = request.POST.get('sender_email')
    sender_name = request.POST.get('sender_name')
    message = request.POST.get('message')
    subject = 'New contact request'
    body = render_to_string(
            'contact/emails/contact_body.txt',
            {
             'sender_email': sender_email,
             'sender_name': sender_name,
             'message': message,
            })
    send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email]
            )
    return redirect(reverse('home'))
