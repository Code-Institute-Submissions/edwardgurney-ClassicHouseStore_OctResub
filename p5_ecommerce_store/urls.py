from django.urls import path
from .views import (StoreFrontView, ProductDetailView, BasketView,
                    CategoryView, CheckoutView, payment_view,
                    create_payment_intent, checkout_complete,
                    rate_record, search_view, SiteMapView,
                    news_letter_subscription)

urlpatterns = [
    path('', StoreFrontView.as_view(), name='home'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(),
         name='product_detail'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('category/<int:pk>', CategoryView.as_view(), name='category'),
    path('checkout/<int:pk>', CheckoutView.as_view(), name='checkout'),
    path('payment/<int:pk>', payment_view, name='payment'),
    path('create-payment-intent/<int:pk>', create_payment_intent,
         name='create_payment_intent'),
    path('checkout-complete/<int:pk>', checkout_complete,
         name='checkout_complete'),
    path('rate-record/<int:pk>', rate_record, name='rate_record'),
    path('search/', search_view, name='search'),
    path('sitemap/', SiteMapView.as_view(), name='sitemap'),
    path('newsletter/', news_letter_subscription, name='newsletter'),
]
