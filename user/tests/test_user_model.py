from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@v8.app', password='password', first_name='Steve', last_name='Jobs')

    def test_user_fullname(self):
        """test the property full name"""
        self.assertEqual('Steve Jobs', self.user.full_name)
