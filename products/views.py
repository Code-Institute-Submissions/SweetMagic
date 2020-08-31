from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    """ A view to display all products on the store """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product(request, product_id):
    """ A view to display a specific product and its details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product.html', context)
