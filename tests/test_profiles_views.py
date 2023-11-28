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
            favorite_city='Test City'
        )


    def test_profile_view(self):
        response = self.client.get(reverse('/profile/', args=['testuser']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.profile.favorite_city)
