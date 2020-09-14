from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


def products(request):
    """ A view to display all products on the store """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sq' in request.GET:
            query = request.GET['sq']
            if not query:
                messages.error(request, "Please enter a valid search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | (
                      Q(description__icontains=query))
            products = products.filter(queries)

    context = {
        'products': products,
        'search_query': query,
        'selected_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product(request, product_id):
    """ A view to display a specific product and its details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product.html', context)


def add_product(request):
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
