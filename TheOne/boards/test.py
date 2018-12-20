from django.core.urlresolvers import reverse
from django.test import TestCase

class HomeTest(TestCase):
    def test_name_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)