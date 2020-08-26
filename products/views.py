from django.shortcuts import render
from .models import Product


def products(request):
    """ A view to display all products on the store """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
