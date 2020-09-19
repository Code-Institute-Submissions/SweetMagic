from django.shortcuts import (redirect, reverse, get_object_or_404)
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from products.models import Product


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
    messages.success(request, 'Contact request submited')
    return redirect(reverse('home'))


def quotation_request(request, item_id):
    redirect_url = request.POST.get('redirect_url')
    recipient_email = "orders.sweetmagic@gmail.com"
    sender_email = request.POST.get('sender_email')
    sender_name = request.POST.get('sender_name')
    product = get_object_or_404(Product, pk=item_id)
    cake_base = None
    if 'cake_base' in request.POST:
        cake_base = request.POST.get('cake_base')
    cake_cream = None
    if 'cake_cream' in request.POST:
        cake_cream = request.POST.get('cake_cream')
    cake_extra = None
    if 'cake_extra' in request.POST:
        cake_extra = request.POST.get('cake_extra')
    request_message = request.POST.get('request_message')
    subject = 'New quotation request'
    body = render_to_string(
            'contact/emails/quotation_body.txt',
            {
             'sender_email': sender_email,
             'sender_name': sender_name,
             'product': product,
             'cake_base': cake_base,
             'cake_cream': cake_cream,
             'cake_extra': cake_extra,
             'request_message': request_message,
            })
    send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email]
            )
    messages.success(request, 'Quotation request submited')
    return redirect(redirect_url)
