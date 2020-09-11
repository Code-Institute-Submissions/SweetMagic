from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HQCbRJUjedNPvz823GYMq559Zyjn0zzGawQA5ILanKb7zSbJG4xKb1CwLLroB61kX5HcYOM48537l4Wrsorm1CK00qCMmcsXi',
        'stripe_client_secret': 'test',
    }

    return render(request, template, context)
