from django.test import TestCase
from django.contrib.auth import get_user_model
from calc import models

class CustomUserTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@v8.app', password='password', first_name='Steve', last_name='Jobs')

    def test_user_fullname(self):
        """test the property full name"""
        self.assertEqual('Steve Jobs', self.user.full_name)

    def test_category_model(self):
        category = models.Category.objects.create(title='Transportation')

        self.assertEqual('Transportation', category.title)

    def test_category_model(self):
        category = models.Category.objects.create(title='Transportation')
        sub_category = models.SubCategory.objects.create(title='Car', category=category)

        self.assertEqual('Transportation', sub_category.category.title)
        self.assertEqual('Car', sub_category.title)
