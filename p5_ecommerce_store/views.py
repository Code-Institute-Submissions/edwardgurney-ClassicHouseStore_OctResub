from django.shortcuts import render
from django.views import generic, View
from .models import Product

class StoreFrontView(generic.ListView):
    template_name = 'p5_ecommerce_store/index.html'
    queryset = Product.objects.all()

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'p5_ecommerce_store/product_detail.html'

class BasketView(View):
    template_name = 'p5_ecommerce_store/basket.html'

    # def get():
    
def basket_view(request):
    return render(request, 'p5_ecommerce_store/basket.html')