from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.models import Product


def my_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    flavour = None
    if 'flavour' in request.POST:
        flavour = request.POST['flavour']
    bag = request.session.get('bag', {})

    if flavour:
        if item_id in list(bag.keys()):
            if flavour in bag[item_id]['items_by_flavour'].keys():
                bag[item_id]['items_by_flavour'][flavour] += quantity
            else:
                bag[item_id]['items_by_flavour'][flavour] = quantity
        else:
            bag[item_id] = {'items_by_flavour': {flavour: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
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
    return redirect(reverse('my_bag'))


def delete_from_bag(request, item_id):
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
    return redirect(reverse('my_bag'))
