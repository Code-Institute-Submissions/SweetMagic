from django.shortcuts import get_object_or_404
from products.models import Product


def favorite_contents(request):
    """Context to make user favorites available throughout the website"""

    favorite_items = []
    favorites = request.session.get('favorites', {})

    for item_id, item_data in favorites.items():
        product = get_object_or_404(Product, pk=item_id)
        favorite_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'favorite_items': favorite_items,
    }

    return context
