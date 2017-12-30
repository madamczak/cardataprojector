from django.test import TestCase
from django.urls import resolve
from cars.views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolvest_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={})
        pass
        self.assertRedirects(None, None)

