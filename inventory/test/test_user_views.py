from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from inventory.models import User
from rest_framework.authtoken.models import Token

class UserViewTests(APITestCase):
    def setUp(self):
        # Create a superuser
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword', email='admin@example.com')
        self.admin_token = Token.objects.create(user=self.admin_user)
        
        # Create a regular user
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        self.token = Token.objects.create(user=self.user)
        
        self.client = APIClient()
        
    def test_list_users(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        url = reverse('user-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        url = reverse('user-list-create')
        new_user_data = {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com',
        }
        response = self.client.post(url, new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)

    def test_retrieve_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        updated_user_data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'password': 'testpassword'
        }
        response = self.client.put(url, updated_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, updated_user_data['username'])
        self.assertEqual(self.user.email, updated_user_data['email'])

    def test_delete_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 1)

    def test_user_login(self):
        url = reverse('user-login')
        login_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)