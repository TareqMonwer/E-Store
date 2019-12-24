from django.test import TestCase
from django.contrib.auth import get_user_model


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
        
