from django.db import models


class Category(models.Model):
    """Defines the category model"""

    class Meta:  # To correct the plural error
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    viewer_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def find_viewer_name(self):
        return self.viewer_name


class Product(models.Model):
    """Defines the products model"""
    name = models.CharField(max_length=254)
    description = models.TextField()
    # Sets default price to all products that require budget
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    # Sets default quantity to all cakes not sold as pack
    quantity = models.IntegerField(default=1)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
