from django import forms
from .models import ShippingAddress
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class AddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ("user",)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")
