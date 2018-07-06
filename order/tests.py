
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class OrderTest(APITestCase):
    def setUp(self):
        """
        Create pizza first.
        """
        url = reverse('pizza')
        data = {
            "name": "Neapolitan",
            "description": "Features tomatoes, garlic, oregano, and extra virgin olive oil"
        }
        self.client.post(url, data, format='json')

    def list_pizza(self):
        """
        list pizza.
        """
        url = reverse('pizza')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def add_pizza(self):
        """
        Create pizza.
        """
        url = reverse('pizza')
        data = {
            "name": "Old Neapolitan",
            "description": "Features tomatoes, garlic, oregano, and extra virgin olive oil"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def update_pizza(self):
        """
        Update pizza.
        """
        url = reverse('pizza', args=[1])
        data = {
            "name": "New Neapolitan",
            "description": "Features tomatoes, garlic, oregano, and extra virgin olive oil"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def delete_pizza(self):
        """
        delete pizza.
        """
        url = reverse('pizza', args=[1])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def list_orders(self):
        """
        list pizza.
        """
        url = reverse('order')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_order(self):
        """
        Ensure we can create a new order.
        """
        url = reverse('order')
        data = {
            "pizza_id": "1",
            "pizza_size": "50",
            "customer_name": "Fady",
            "customer_address": "5 Zakria Gnehom St. Alexandria, Egypt"

        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def update_order(self):
        """
        Ensure we can update an order.
        """
        url = reverse('order', args=[1])
        data = {
            "pizza_id": "1",
            "pizza_size": "30",
            "customer_name": "Fady Alfred",
            "customer_address": "5 Zakria Gnehom St. Alexandria, Egypt"

        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def delete_order(self):
        """
        delete pizza.
        """
        url = reverse('order', args=[1])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def list_customer_orders(self):
        """
        list pizza.
        """
        url = reverse('customer', args=['Fady Alfred'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test(self):
        self.add_pizza()
        self.list_pizza()
        self.update_pizza()
        self.create_order()
        self.list_orders()
        self.update_order()
        self.list_customer_orders()
        self.delete_order()
        self.delete_pizza()

