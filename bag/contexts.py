

def bag_contents(request):

    bag_items = []
    total = 0
    number_of_products = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'number_of_products': number_of_products,
    }

    return context
