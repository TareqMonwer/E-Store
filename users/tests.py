from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupView


class CustomUserTest(TestCase):

    def test_user_create(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            password='321nop4a55',
            email='testuser@nomail.com'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='super',
            password='n0p4s5w0rd',
            email='super@man.marvel'
        )
        self.assertEqual(admin_user.username, 'super')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        


class SignupPageTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.resp = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.resp.status_code, 200)
        self.assertContains(self.resp, 'Create New Account')
        self.assertNotContains(self.resp, 'Go away')
        self.assertTemplateUsed('signup.html')
    
    def test_signup_resolve_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupView.as_view().__name__
        )
    
    def test_signup_form(self):
        form = self.resp.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)