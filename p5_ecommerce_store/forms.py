from django import forms
from .models import ShippingAddress

class AddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ("user",)