from django.test import TestCase, Client
from django.urls import reverse
from letting.models import Letting, Address

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

    def test_letting_view(self):
        client = Client()
        letting = Letting.objects.get(id=1)
        response = client.get(reverse('letting', args=[letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'letting.html')
        self.assertEqual(response.context['title'], letting.title)
        self.assertEqual(response.context['address'], letting.address)