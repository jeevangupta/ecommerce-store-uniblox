from django.test import TestCase
import json
from .views import add_to_cart


class AddToCartTest(TestCase):

    def test_add_to_cart_success(self):
        # Valid product data
        data = {"id": 1, "name": "Test Product", "price": 100}

        # Simulate a POST request with JSON data
        response = self.client.post('/shoesvilla/add-to-cart/', data=json.dumps(data), content_type='application/json')

        # Assert expected response status code (200 for success)
        self.assertEqual(response.status_code, 200)

        # Assert response data contains added product and status
        expected_response = {
            "status": True,
            "product_store": {
                str(data["id"]): {
                    "name": data["name"],
                    "price": data["price"]
                }
            },
            "discount_details": {"discount_code": "", "discount": "0"}
        }
        self.assertEqual(response.data, expected_response)


    def test_add_to_cart_invalid_data(self):
        # Invalid data (missing price)
        data = {"id": 1, "name": "Test Product"}

        # Simulate a POST request
        response = self.client.post('/shoesvilla/add-to-cart/', data=json.dumps(data), content_type='application/json')

        # Assert expected status code for bad request (e.g., 400)
        self.assertEqual(response.status_code, 400)
