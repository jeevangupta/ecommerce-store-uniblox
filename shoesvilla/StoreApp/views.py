from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
# Define an in-memory store using a dictionary
product_store = {}


def home(request):

    user = request.user

    #return HttpResponse("Hello World !")
    return render(request, "./home.html")

#api end point function to handle adding item to cart
def add_to_cart(request):
    request_body = request.body
    body_unicode = request_body.decode("utf-8")
    body_unicode = json.loads(body_unicode)
    status = False

    product_store[body_unicode["id"]] = {'name': body_unicode["name"], 'price': int(body_unicode["price"])}

    status = True

    return JsonResponse({"status":status, "product_store": product_store})
