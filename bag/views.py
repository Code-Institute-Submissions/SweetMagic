from django.shortcuts import render, redirect


def my_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
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

    request.session['bag'] = bag
    return redirect(redirect_url)
