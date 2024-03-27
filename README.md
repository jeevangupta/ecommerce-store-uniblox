
Functionality

Client APIs:
    Add items to cart
    Checkout with optional discount code application (validated for nth order)

Admin APIs:
    Generate a discount code (if applicable based on order count)
    Retrieve purchase statistics (item count, total purchase amount, discount codes, total discount amount)

Stretch Goal: Building a UI for the store functionality (using a framework of choice)

Technologies Used: Python with Django REST Framework, HTML, CSS, JavaScript/jQuery

Get Started:
1. Clone this repository.
2. Install required dependencies
3. Run the application
    python3 manage.py runserver

    To access the home page use -> http://127.0.0.1:8000/shoesvilla/

    Once you are home page you will see bunch of product with an button "add to cart"

    When you click on button "add to cart", you will see a pop-up giving the status of action


    On top right side you will see "CART"
    on click on that you will see a pop-up displaying the list of items in the cart with discount if applicable.

    You will also see button to checkout

    when you click on "checkout" button you will see a pop-up with action status and details

    

