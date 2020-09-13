from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin (admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product_total',)


class OrderAdmin (admin.ModelAdmin):
    inlines = (OrderItemAdmin,)

    readonly_fields = ('order_number', 'order_date',
                       'order_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'full_name', 'email',
              'phone_number', 'street_address',
              'post_code', 'town_or_city',
              'country', 'order_date', 'order_total',
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'full_name',
                    'order_date', 'order_total',)

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
