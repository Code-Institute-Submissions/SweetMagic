from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def my_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    flavour = None
    if 'flavour' in request.POST:
        flavour = request.POST['flavour']
    notes = request.POST.get('notes')
    bag = request.session.get('bag', {})

    if flavour:
        if item_id in list(bag.keys()):
            if flavour in bag[item_id]['items_by_flavour'].keys():
                bag[item_id]['items_by_flavour'][flavour] += quantity
                messages.success(request, f'{product.name}<br>\
                    {product.price}€<br>Flavour: {flavour}<br>\
                        Total quantity: \
                            {bag[item_id]["items_by_flavour"][flavour]}')
            else:
                bag[item_id]['items_by_flavour'][flavour] = quantity
                messages.success(request, f'{product.name}<br>\
                    {product.price}€<br>Flavour: {flavour}<br>\
                        Total quantity: \
                            {bag[item_id]["items_by_flavour"][flavour]}')
        else:
            bag[item_id] = {'items_by_flavour': {flavour: quantity}}
            messages.success(request, f'{product.name}<br>\
                {product.price}€<br>Flavour: {flavour}<br>\
                    Total quantity: \
                        {bag[item_id]["items_by_flavour"][flavour]}')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'{product.name}<br>\
                {product.price}€<br>Total quantity: {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name}<br>\
                {product.price}€<br>Total quantity: {bag[item_id]}')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    flavour = None
    if 'flavour' in request.POST:
        flavour = request.POST['flavour']
    bag = request.session.get('bag', {})

    if flavour:
        if quantity > 0:
            bag[item_id]['items_by_flavour'][flavour] = quantity
        else:
            del bag[item_id]['items_by_flavour'][flavour]
            if not bag[item_id]['items_by_flavour']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(redirect_url)


def delete_from_bag(request, item_id):
    redirect_url = request.POST.get('redirect_url')
    flavour = None
    if 'flavour' in request.POST:
        flavour = request.POST['flavour']
    bag = request.session.get('bag', {})
    if flavour:
        del bag[item_id]['items_by_flavour'][flavour]
        if not bag[item_id]['items_by_flavour']:
            bag.pop(item_id)
    else:
        bag.pop(item_id)
    request.session['bag'] = bag
    return redirect(redirect_url)
