from decimal import Decimal
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from inventory.models import User, Product
from rest_framework.authtoken.models import Token

class ProductViewTests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        self.client = APIClient()
        
        # Authenticate the user
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Create a product
        self.product_data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': '100.00'
        }
        self.product_instance = Product.objects.create(**self.product_data)

    def test_list_products(self):
        url = reverse('product-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_product(self):
        url = reverse('product-list-create')
        new_product_data = {
            'name': 'New Product',
            'description': 'This is a new product',
            'price': '200.00'
        }
        response = self.client.post(url, new_product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_retrieve_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product_instance.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product_instance.name)

    def test_update_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product_instance.pk})
        updated_product_data = {
            'name': 'Updated Product',
            'description': 'This is an updated product',
            'price': '150.00'
        }
        response = self.client.put(url, updated_product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product_instance.refresh_from_db()
        self.assertEqual(self.product_instance.name, updated_product_data['name'])
        self.assertEqual(self.product_instance.description, updated_product_data['description'])
        self.assertEqual(self.product_instance.price, Decimal(updated_product_data['price']))

    def test_delete_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product_instance.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
