
Shoesvilla API

    This API provides functionalities for managing a shoe store inventory and processing customer orders.

Features

    Client APIs
        Add items to cart
        Checkout with optional discount code application (validated based on order count)
    
    Admin APIs
        Generate discount code (if applicable based on order criteria)
        Retrieve purchase statistics (item count, total purchase amount, discount codes used, total discount amount)

    Stretch Goal (future implementation)
        Building a user interface (UI) for the store functionality using a preferred framework
        Technologies Used

    Backend: Python with Django REST Framework
    
    Frontend: HTML, CSS, JavaScript/jQuery

Getting Started

    1. Clone the repository
    2. Install dependencies (refer to documentation for specific commands)
    3. Run the application
        python3 manage.py runserver

Access the API
    Browse to http://127.0.0.1:8000/shoesvilla/ in your web browser.

Client Functionality

    - The home page displays a list of products.
    - Clicking the "add to cart" button adds the item to your cart and displays a confirmation popup.
    - The top right corner displays a "CART" button.
    - Clicking the "CART" button shows a popup with the list of items in your cart and any applicable discounts.
    - The cart popup also provides a "checkout" button.
    - Clicking the "checkout" button initiates the checkout process and displays a confirmation popup with details.
