from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import Profile

class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = get_user_model().objects.create_user(
            username='testuser', password='testpass'
        )
        Profile.objects.create(user=user, favorite_city='San Francisco')

    def test_user_label(self):
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'user')

    def test_favorite_city_label(self):
        profile = Profile.objects.get(id=1)
        field_label = profile._meta.get_field('favorite_city').verbose_name
        self.assertEquals(field_label, 'favorite city')

    def test_favorite_city_max_length(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('favorite_city').max_length
        self.assertEquals(max_length, 64)

    def test_object_name_is_username(self):
        profile = Profile.objects.get(id=1)
        expected_object_name = f'{profile.user.username}'
        self.assertEquals(expected_object_name, str(profile))