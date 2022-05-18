from django.test import TestCase, RequestFactory
from animais.views import index

class AnimaisTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_url(self):
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)