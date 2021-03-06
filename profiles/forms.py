from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    """Form to update (or add is there is none) profile information"""
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address': 'Street Address',
            'default_post_code': 'Postal Code',
            'default_town_or_city': 'Town or City',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = (
                    'stripe_style_input input-border rounded-0')
            else:
                self.fields[field].widget.attrs['class'] = (
                    'stripe_style_input input-border rounded-0 my-select')
            self.fields[field].label = False
