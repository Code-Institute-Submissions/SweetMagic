from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_product(request):
    """A view to display add product page"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(reverse('product', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                                     Please double check the form.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_product(request, product_id):
    """A view to display edit product page"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                                     Please double check the form.')
    else:
        form = ProductForm(instance=product)

    template = 'products/update_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """A view to delete product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('products'))
