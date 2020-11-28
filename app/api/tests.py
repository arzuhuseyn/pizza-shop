import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from catalog.models import Pizza, Ingredient
from orders.models import OrderProfile, Order


class OrderTests(APITestCase):
    def test_create_order(self):
        
        customer = OrderProfile.objects.create(
            name='Arzu',
            surname='Huseynov',
            address='Baker str 221B',
            phone='00994508742022'
        )

        pizza_item1 = Pizza.objects.create(name='Margaritta')
        pizza_item2 = Pizza.objects.create(name='Margaritta2')

        ingredient1 = Ingredient.objects.create(name='Cheese')
        ingredient2 = Ingredient.objects.create(name='More cheese')

        url = reverse('create-order')
        data = {
            'customer_id' : customer.id,
            'items' : [
                {'id': pizza_item1.id, 'size' : 'm', 'count': 2, 'ingredients': [ingredient1.id, ingredient2.id]},
                {'id': pizza_item2.id, 'size' : 'l', 'count': 1, 'ingredients': [ingredient2.id]},
                {'id': pizza_item2.id, 'size' : 's', 'count': 5, 'ingredients': [ingredient1.id]}
        ]}
        
        response = self.client.post(url, data, 'json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().customer, customer)
        self.assertEqual(Order.objects.get().status, 0)
        self.assertEqual(len(Order.objects.get().items), len(data.get('items')))