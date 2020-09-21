from django.shortcuts import render, redirect
from django.contrib import messages


def my_favorites(request):
    """View to display user favorite products"""
    return render(request, 'favorites/favorites.html')


def add_to_favorites(request, item_id):
    """View to add user favorite products"""
    redirect_url = request.POST.get('redirect_url')
    quantity = 1
    favorites = request.session.get('favorites', {})

    if item_id in list(favorites.keys()):
        messages.info(request, 'Product already in your favorites')

    else:
        favorites[item_id] = favorites.get(item_id, quantity)
        messages.success(request, 'Added product to favorites')

    request.session['favorites'] = favorites
    return redirect(redirect_url)


def remove_from_favorites(request, item_id):
    """View to remove product from user favorite products"""
    redirect_url = request.POST.get('redirect_url')
    favorites = request.session.get('favorites', {})

    favorites.pop(item_id)

    request.session['favorites'] = favorites
    return redirect(redirect_url)
