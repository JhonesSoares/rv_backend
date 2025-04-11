from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from core.models import User

class JWTAuthenticationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            password='123456',  # Você pode usar make_password se precisar de hash
            type='common'
        )

    def test_token_obtain_pair(self):
        response = self.client.post('/api/token/', {
            'email': 'test@example.com',
            'password': '123456'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_access_protected_view(self):
        # Obter token
        response = self.client.post('/api/token/', {
            'email': 'test@example.com',
            'password': '123456'
        })
        token = response.data['access']

        # Enviar requisição autenticada
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        protected_response = self.client.get('/api/users/')

        self.assertEqual(protected_response.status_code, status.HTTP_200_OK)


        ### VERIFICAR TESTES UNITARIOS DE AUTENTICAÇÃO
         