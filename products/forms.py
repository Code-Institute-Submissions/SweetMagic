from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Form to be used in add product and edit product functionallity"""

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        viewer_names = [(c.id, c.find_viewer_name()) for c in categories]

        self.fields['category'].choices = viewer_names
        for field_name, field in self.fields.items():
            if field_name != 'image':
                field.widget.attrs['class'] = 'rounded-0 input-border'
            else:
                field.widget.attrs['class'] = 'border-0'
