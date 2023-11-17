from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            bio='Test bio',
            location='Test location',
            birth_date='2000-01-01'
        )

    def test_profile_view(self):
        response = self.client.get(reverse('profile', args=['testuser']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, 'Test bio')
        self.assertContains(response, 'Test location')
        self.assertContains(response, '2000-01-01')