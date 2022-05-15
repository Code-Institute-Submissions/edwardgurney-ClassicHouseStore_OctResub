from django import forms
from .models import ShippingAddress, NewsLetterSubs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class AddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ("user",)


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Re-type Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterSubs
        exclude = ("subscription_date",)