from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import Profile


class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        cls.profile = Profile.objects.create(user=cls.user, favorite_city='San Francisco')

    def test_user_label(self):
        # Test the label of the 'user' field
        field_label = self.profile._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_favorite_city_label(self):
        # Test the label of the 'favorite_city' field
        field_label = self.profile._meta.get_field('favorite_city').verbose_name
        self.assertEqual(field_label, 'favorite city')

    def test_favorite_city_max_length(self):
        # Test the max length of the 'favorite_city' field
        max_length = self.profile._meta.get_field('favorite_city').max_length
        self.assertEqual(max_length, 64)

    def test_object_name(self):
        # Test the object name of the profile
        expected_object_name = f'{self.profile.user.username}'
        self.assertEqual(str(self.profile), expected_object_name)
