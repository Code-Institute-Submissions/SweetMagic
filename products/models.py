from django.db import models


class Category(models.Model):

    class Meta:  # To correct the plural error
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    viewer_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def find_viewer_name(self):
        return self.viewer_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
