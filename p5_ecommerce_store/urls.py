from django.urls import path
from .views import StoreFrontView, ProductDetailView, BasketView, basket_view

urlpatterns = [
    path('', StoreFrontView.as_view(), name='home'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    # path('basket/', BasketView.as_view(), name='basket'),
    path('basket/', basket_view, name='basket'),

]