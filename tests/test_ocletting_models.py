from django.test import TestCase
from oc_letting_site.models import Address

class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Address.objects.create(
            number=123,
            street='Main St',
            city='Anytown',
            state='CA',
            zip_code=12345,
            country_iso_code='USA'
        )

    def test_number_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_street_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('street').verbose_name
        self.assertEquals(field_label, 'street')

    def test_city_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'city')

    def test_state_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('state').verbose_name
        self.assertEquals(field_label, 'state')

    def test_zip_code_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('zip_code').verbose_name
        self.assertEquals(field_label, 'zip code')

    def test_country_iso_code_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('country_iso_code').verbose_name
        self.assertEqual(field_label, 'country iso code')


    def test_number_max_value(self):
        address = Address.objects.get(id=1)
        max_value = address._meta.get_field('number').validators[0].limit_value
        self.assertEquals(max_value, 9999)

    def test_zip_code_max_value(self):
        address = Address.objects.get(id=1)
        max_value = address._meta.get_field('zip_code').validators[0].limit_value
        self.assertEquals(max_value, 99999)

    def test_state_min_length(self):
        address = Address.objects.get(id=1)
        min_length = address._meta.get_field('state').validators[0].limit_value
        self.assertEquals(min_length, 2)

    def test_country_iso_code_min_length(self):
        address = Address.objects.get(id=1)
        min_length = address._meta.get_field('country_iso_code').validators[0].limit_value
        self.assertEquals(min_length, 3)

    def test_object_name_is_number_and_street(self):
        address = Address.objects.get(id=1)
        expected_object_name = f'{address.number} {address.street}'
        self.assertEquals(expected_object_name, str(address))