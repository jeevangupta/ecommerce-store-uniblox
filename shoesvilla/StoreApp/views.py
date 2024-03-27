from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
# Define an in-memory store using a dictionary
product_store = {}
discount_codes = ["","jk12","sds21","fm84"]

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

    #call admin api to generate a discount code if the condition is satisfied.
    # ideally this will be done when items are added in cart
    #lets assume there is object that keep record of all valid code
    discount_code = "jk12"
    discount = "10%"

    discount_code = ""
    discount = "0"

    discount_details = {"discount_code":discount_code,"discount":discount}

    status = True

    return JsonResponse({"status":status, "product_store": product_store, "discount_details":discount_details})


def checkout(request):
    request_body = request.body
    body_unicode = request_body.decode("utf-8")
    body_unicode = json.loads(body_unicode)
    status = False

    discount_details = body_unicode["discount_details"]

    code = discount_details.get("discount_code",None)
    
    #Lists count of items purchased, total purchase amount, list of discount codes and total discount amount.
    #assuming I have list of discount codes
    #I will check the validity of discount code in payload
    if(code in discount_codes):
        #with above api will get the total amount and discount amount
        #for now below i will have code to calculate it
        
        discount_str = discount_details["discount"]  # Discount percentage as a string
        # Convert discount percentage string to a numerical value
        discount_percentage = float(discount_str.strip('%'))

        # Calculate total amount
        total_amount = 0
        products = list(product_store.values())
        product_store.clear()

        for product in products:
            total_amount += product['price']

        # Calculate discount amount
        discount_amount = (total_amount * discount_percentage) / 100

        # Calculate final amount after discount
        final_amount = total_amount - discount_amount
        status = True
        mssg = f"ORDER PLACED \n Final amount : ₹{final_amount} \n Discount amount: ₹{discount_amount}"

        #reset the product_store
        #product_store = {}
    else:
        mssg = "Invalid Discount Code"
        status = False

    return JsonResponse({"status":status, "mssg": mssg })
