from django.test import TestCase, RequestFactory
from django.urls import reverse
from letting.models import Letting, Address
from letting.views import letting
from django.http import Http404

class LettingViewTest(TestCase):
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

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_letting_view(self):
        # Create an instance of a GET request.
        request = self.factory.get(reverse('letting', args=[1]))

        # Use the request to get the response.
        response = letting(request, 1)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the expected title and address.
        self.assertContains(response, 'Test Letting')
        self.assertContains(response, '123 Main St')

    def test_letting_view_invalid_id(self):
        # Create an instance of a GET request with an invalid letting ID.
        request = self.factory.get(reverse('letting', args=[999]))

        # Use the request to get the response and check for Http404 exception.
        with self.assertRaises(Http404):
            _ = letting(request, 999)