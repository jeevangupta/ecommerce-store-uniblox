from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
import uuid

# Define an in-memory store using a dictionary
users = []
product_store = {}
discount_codes = ["","jk12","sds21","fm84"]
codes = {}

def home(request):

    if 'user' in request:
        user_id = request.user
    else:
        user_id = str(uuid.uuid4())
        request.user = user_id

    users.append(user_id)

    data = {'user_id': user_id}

    return render(request, "./home.html", data)


#api end point function to handle adding item to cart
def add_to_cart(request):
    if request.method == 'POST':
        body = decode_payload(request)
        user_id = body["user_id"]
        name = body["name"]
        price = int(body["price"])
        status = False
        mssg = ""

        if user_id in users: 
            if user_id in product_store:
                product_store[user_id][body["id"]] = {'name': name, 'price': price}
            else:
                product_store[user_id] = {body["id"]: {'name': name, 'price': price}}
            status = True
        else:
            status = False
            mssg = "Invalid User"

        return JsonResponse({"status":status, "mssg":mssg, "product_store": product_store})
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)


def generate_discount_code(request):
    #call admin api to generate a discount code if the condition is satisfied.
    #ideally this will be done when items are added in cart
    #lets assume there is object that keep record of all valid code
    
    if request.method == 'POST':
        body = decode_payload(request)
        user_id = body["user_id"]
        status = False

        discount_code = ""
        discount = "0"
        
        if user_id in users:
            
            if user_id in product_store:
                status = True

                products = list(product_store[user_id].values())
                product_count = len(products)
                total_amount = 0

                for product in products:
                    total_amount += product['price']

                if product_count >= 2 and total_amount >= 3000:
                    discount_code = '24DISCOUNT10'
                    discount = "10%"
            
                codes[discount_code] = discount

        discount_details = {"discount_code":discount_code,"discount":discount}

        return JsonResponse({"status": status, "discount_details": discount_details})
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)


def checkout(request):
    body = decode_payload(request)
    status = False
    user_id = body["user_id"]
    code = body["discount_code"]
    
    #Lists count of items purchased, total purchase amount, list of discount codes and total discount amount.
    #assuming I have list of discount codes
    if  user_id in users:
        if(code in codes):
            discount_str = codes[code]  # Discount percentage as a string
            # Convert discount percentage string to a numerical value
            discount_percentage = float(discount_str.strip('%'))

            # Calculate total amount
            total_amount = 0
            products = list(product_store[user_id].values())
            product_store.clear()

            total_amount = sum(product['price'] for product in products)


            # Calculate discount amount
            discount_amount = (total_amount * discount_percentage) / 100

            # Calculate final amount after discount
            final_amount = total_amount - discount_amount
            status = True
            mssg = f"ORDER PLACED \n Final amount : ₹{final_amount} \n Discount amount: ₹{discount_amount}"

        else:
            mssg = "Invalid Discount Code"
    else:
        mssg = "Invalid User"

    return JsonResponse({"status":status, "mssg": mssg })


def decode_payload(request):
    request_body = request.body
    body_unicode = request_body.decode("utf-8")
    body_unicode = json.loads(body_unicode)

    return body_unicode