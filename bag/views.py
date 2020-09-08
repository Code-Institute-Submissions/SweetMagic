from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
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
    bag = request.session.get('bag', {})

    if flavour:
        if item_id in list(bag.keys()):
            if flavour in bag[item_id]['items_by_flavour'].keys():
                bag[item_id]['items_by_flavour'][flavour] += quantity
                messages.success(request, f'Updated {product.name} with {flavour} quantity to {bag[item_id]["items_by_flavour"][flavour]}')
            else:
                bag[item_id]['items_by_flavour'][flavour] = quantity
                messages.success(request, f'Added {product.name} with {flavour} to your bag')
        else:
            bag[item_id] = {'items_by_flavour': {flavour: quantity}}
            messages.success(request, f'Added {product.name} with {flavour} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    flavour = None
    if 'flavour' in request.POST:
        flavour = request.POST['flavour']
    bag = request.session.get('bag', {})

    if flavour:
        if quantity > 0:
            bag[item_id]['items_by_flavour'][flavour] = quantity
            messages.success(request, f'Updated {product.name} with {flavour} quantity to {bag[item_id]["items_by_flavour"][flavour]}')
        else:
            del bag[item_id]['items_by_flavour'][flavour]
            if not bag[item_id]['items_by_flavour']:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} with {flavour} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def delete_from_bag(request, item_id):

    try:
        product = get_object_or_404(Product, pk=item_id)
        redirect_url = request.POST.get('redirect_url')
        flavour = None
        if 'flavour' in request.POST:
            flavour = request.POST['flavour']
        bag = request.session.get('bag', {})

        if flavour:
            del bag[item_id]['items_by_flavour'][flavour]
            if not bag[item_id]['items_by_flavour']:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} with {flavour} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return redirect(redirect_url)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
