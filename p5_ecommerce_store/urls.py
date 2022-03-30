from django.urls import path
from .views import StoreFrontView

urlpatterns = [
    path('', StoreFrontView.as_view(), name='home'),
]