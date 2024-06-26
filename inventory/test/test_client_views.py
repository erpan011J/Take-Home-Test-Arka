from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from inventory.models import User, Client
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal


class ClientViewTests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        self.client = APIClient()
        
        # Authenticate the user
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Create a client
        self.client_data = {
            'user': self.user,
            'start_date': timezone.now().date() - timedelta(days=30),
            'contract_value': '10000.00'
        }
        self.client_instance = Client.objects.create(**self.client_data)

    def test_list_clients(self):
        url = reverse('client-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_client(self):
        url = reverse('client-list-create')
        new_client_data = {
            'user': self.user.id,
            'start_date': timezone.now().date(),
            'contract_value': '5000.00'
        }
        response = self.client.post(url, new_client_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 2)

    def test_retrieve_client(self):
        url = reverse('client-detail', kwargs={'pk': self.client_instance.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], self.client_instance.user.id)

    def test_update_client(self):
        url = reverse('client-detail', kwargs={'pk': self.client_instance.pk})
        updated_client_data = {
            'user': self.user.id,
            'start_date': self.client_instance.start_date,
            'contract_value': '15000.00'
        }
        response = self.client.put(url, updated_client_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client_instance.refresh_from_db()
        self.assertEqual(self.client_instance.contract_value, Decimal(updated_client_data['contract_value']))

    def test_delete_client(self):
        url = reverse('client-detail', kwargs={'pk': self.client_instance.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Client.objects.count(), 0)
