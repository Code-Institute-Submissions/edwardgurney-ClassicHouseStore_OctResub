from django.urls import path
from .views import StoreFrontView, ProductDetailView, BasketView, CategoryView, CheckoutView


urlpatterns = [
    path('', StoreFrontView.as_view(), name='home'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('category/<int:pk>', CategoryView.as_view(), name='category'),
    path('checkout/<int:pk>', CheckoutView.as_view(), name='checkout'),
    

]