from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


def products(request):
    """ A view to display all products on the store """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'sq' in request.GET:
            query = request.GET['sq']
            if not query:
                messages.error(request, "Please enter a valid search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_query': query,
    }

    return render(request, 'products/products.html', context)


def product(request, product_id):
    """ A view to display a specific product and its details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product.html', context)
