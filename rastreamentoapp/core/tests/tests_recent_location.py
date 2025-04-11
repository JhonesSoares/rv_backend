from django.test import TestCase
from rest_framework.test import APIClient
from django.utils import timezone
from datetime import timedelta
from core.models import User, Vehicle, Location

class VehicleTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name='John',
            email='john@email.com',
            password='123',
            type='common'
        )
        self.vehicle = Vehicle.objects.create(
            user=self.user,
            plate='ABC1234',
            model='Civic',
            status='online'
        )
        Location.objects.create(
            vehicle=self.vehicle,
            latitude=1.23,
            longitude=4.56,
            speed=50,
            timestamp=timezone.now()
        )

    def test_recent_locations(self):
        url = f'/api/vehicles/{self.vehicle.id}/recent_locations/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)