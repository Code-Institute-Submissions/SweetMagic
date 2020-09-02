from django.shortcuts import render


def my_bag(request):
    return render(request, 'bag/bag.html')
