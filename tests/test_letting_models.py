from django.test import TestCase
from letting.models import Letting, Address


class LettingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        address = Address.objects.create(
            number=1,
            street='123 Main St',
            city='Anytown',
            state='CA',
            zip_code='12345'
        )
        Letting.objects.create(title='Test Letting', address=address)

    def test_title_label(self):
        letting = Letting.objects.get(id=1)
        field_label = letting._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_address_label(self):
        letting = Letting.objects.get(id=1)
        field_label = letting._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_title_max_length(self):
        letting = Letting.objects.get(id=1)
        max_length = letting._meta.get_field('title').max_length
        self.assertEqual(max_length, 256)

    def test_object_name_is_title(self):
        letting = Letting.objects.get(id=1)
        expected_object_name = f'{letting.title}'
        self.assertEqual(expected_object_name, str(letting))
