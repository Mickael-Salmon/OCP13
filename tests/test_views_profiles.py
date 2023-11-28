from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser1', password='testpassword')
        Profile.objects.create(user=self.user, favorite_city='Test city')
        self.client = Client()

    def tearDown(self):
        User.objects.filter(username='testuser1').delete()


    def test_profile_view(self):
        # Create a client to make requests
        client = Client()

        # Log in the user
        client.login(username='testuser1', password='testpassword')

        # Utilise self.client.get au lieu de créer une instance de RequestFactory
        response = self.client.get(reverse('profile', args=['testuser1']))

        # Test assertions
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profiles.html')