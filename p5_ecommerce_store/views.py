from django.shortcuts import render
from django.views import generic
from .models import Product

class StoreFrontView(generic.ListView):
    template_name = 'p5_ecommerce_store/index.html'
    queryset = Product.objects.all()
