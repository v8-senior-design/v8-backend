from django.test import TestCase
from django.contrib.auth import get_user_model
from calc import models

class CustomUserTest(TestCase):
    def test_category_model(self):
        category = models.Category.objects.create(title='Transportation')

        self.assertEqual('Transportation', category.title)

    def test_category_model(self):
        category = models.Category.objects.create(title='Transportation')
        sub_category = models.SubCategory.objects.create(title='Car', category=category)

        self.assertEqual('Transportation', sub_category.category.title)
        self.assertEqual('Car', sub_category.title)
