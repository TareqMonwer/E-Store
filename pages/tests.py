from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        self.resp = self.client.get(reverse("home"))

    def test_homepage_status_code(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_hompage_template(self):
        self.assertTemplateUsed(self.resp, "home.html")

    def test_homepage_contains(self):
        self.assertContains(self.resp, "Home Page")

    def test_homepage_not_contains(self):
        self.assertNotContains(self.resp, "No more bugs todat :P")

    def test_homepage_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

