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
        user_quantity = request.GET.get('quantity', 1)
        current_product = get_object_or_404(Product, id=product_id)
        if user_quantity > 0:
            current_bag_item, created = BagItem.objects.get_or_create(bag=current_bag, product=current_product)
            current_bag_item.quantity = user_quantity
            current_bag_item.save()
        else:
            try:
                bag_item = BagItem.objects.get(bag=current_bag,  product=current_product)
                bag_item.delete()
            except BagItem.DoesNotExist:
                pass

    def get_object(self):
        old_bag_id = self.request.session.get('bag_id', None)
        if old_bag_id is None:
            bag = Bag()
            bag.save()
            self.request.session['bag_id'] = bag.id
        else:
            bag = Bag.objects.get(id=old_bag_id)
        return bag



    
# def basket_view(request):
#     return render(request, 'p5_ecommerce_store/basket.html')
