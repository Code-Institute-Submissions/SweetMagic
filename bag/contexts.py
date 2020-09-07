from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    number_of_products = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            number_of_products += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for flavour, quantity in item_data['items_by_flavour'].items():
                total += quantity * product.price
                number_of_products += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'flavour': flavour,
                })

    context = {
        'bag_items': bag_items,
        'total': total,
        'number_of_products': number_of_products,
    }

    return context
