from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import Profile

# Set up non-modified objects used by all test methods
user = get_user_model().objects.create_user(username='testuser', password='testpass')
Profile.objects.create(user=user, favorite_city='San Francisco')

# Test the label of the 'user' field
profile = Profile.objects.get(id=1)
field_label = profile._meta.get_field('user').verbose_name
assert field_label == 'user'

# Test the label of the 'favorite_city' field
field_label = profile._meta.get_field('favorite_city').verbose_name
assert field_label == 'favorite city'

# Test the max length of the 'favorite_city' field
max_length = profile._meta.get_field('favorite_city').max_length
assert max_length == 64

# Test the object name of the profile
expected_object_name = f'{profile.user.username}'
assert expected_object_name == str(profile)