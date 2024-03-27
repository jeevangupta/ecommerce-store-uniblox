
from django.urls import path
from .views import (home, add_to_cart, checkout)

urlpatterns = [
    path("", home, name="home"),

    path(r"add-to-cart/", add_to_cart, name="add-to-cart"),

    path(r"checkout/", checkout, name="checkout")
]