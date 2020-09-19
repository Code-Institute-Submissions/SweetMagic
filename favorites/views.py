from django.shortcuts import render


def my_favorites(request):
    return render(request, 'favorites/favorites.html')