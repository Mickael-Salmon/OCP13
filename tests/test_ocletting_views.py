from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_content(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'Welcome', response.content)

    def test_index_view_error_handling(self):
        response = self.client.get('/nonexistent-url')
        self.assertEqual(response.status_code, 404)

    def test_index_view_without_login(self):
        response = self.client.get(reverse('index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
