import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product


class Order(models.Model):

    order_number = models.CharField(max_length=30, null=False, editable=False)
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    order_date = models.DateField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = self.items.aggregate(Sum('product_total'))['product_total__sum']
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_flavour = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    product_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.product_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_number}'
