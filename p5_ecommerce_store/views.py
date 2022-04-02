from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product, Bag, BagItem


class StoreFrontView(generic.ListView):
    template_name = 'p5_ecommerce_store/index.html'
    queryset = Product.objects.all()

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'p5_ecommerce_store/product_detail.html'

class BasketView(View):
    template_name = 'p5_ecommerce_store/basket.html'
    model = Bag

    def get(self, request, *args, **kwargs):
        current_bag = self.get_object()
        product_id = request.GET.get('product_id')
        user_quantity = request.GET.get('quantity')
        current_product = get_object_or_404(Product, id=product_id)
        current_bag_item, created = BagItem.objects.get_or_create(bag=current_bag, product=current_product)
        current_bag_item.quantity = user_quantity
        current_bag_item.save()
    
# def basket_view(request):
#     return render(request, 'p5_ecommerce_store/basket.html')
