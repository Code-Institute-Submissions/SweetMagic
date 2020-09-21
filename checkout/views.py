from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from bag.contexts import bag_contents
from products.models import Product
from .models import Order, OrderItem
from .forms import OrderForm
from profiles.models import UserProfile
from profiles.forms import ProfileForm
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_order': request.POST.get('save_order'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, there was an error processing your \
            payment. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """View to display checkout page"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address': request.POST['street_address'],
            'post_code': request.POST['post_code'],
            'town_or_city': request.POST['town_or_city'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = get_object_or_404(Product, pk=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_item.save()
                    else:
                        for (flavour, quantity) in (
                                item_data['items_by_flavour'].items()):

                            order_item = OrderItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_flavour=flavour,
                            )
                            order_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products you were trying to \
                            buy was not found. "
                        "Please contact us for assistance."
                    ))
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_order'] = 'save_order'
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))

        else:
            messages.error(request, "There was an error with your form. \
                Please double check your information.")

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at \
                the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address': profile.default_street_address,
                    'post_code': profile.default_post_code,
                    'town_or_city': profile.default_town_or_city,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """View to display successfull checkout page"""
    save_order = request.session.get('save_order')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_order:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address': order.street_address,
                'default_post_code': order.post_code,
                'default_town_or_city': order.town_or_city,
                'default_country': order.country,
            }
            profile_form = ProfileForm(profile_data, instance=profile)
            if profile_form.is_valid():
                profile_form.save()

    messages.success(request, f'Order successfully made! \
        Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
