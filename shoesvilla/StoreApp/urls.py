
from django.urls import path
from .views import (home, add_to_cart, generate_discount_code, checkout)

urlpatterns = [
    path(r"", home, name="home"),

    path(r"add-to-cart/", add_to_cart, name="add-to-cart"),

    path(r"get-discount-code/", generate_discount_code, name="get-discount-code"),

    path(r"checkout/", checkout, name="checkout")
]