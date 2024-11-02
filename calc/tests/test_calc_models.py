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

class EmissionCategoryTest(TestCase):
    def test_emission_category(self):
        category = EmissionCategory.objects.create(name="Fuel")
        self.assertEqual(category.name, "Electricity")

    def test_name(self):
        EmissionCategory.objects.create(name="Fuel")
        with self.assertRaises(Exception):
            EmissionCategory.objects.create(name="Fuel")

class EmissionFactorTest(TestCase):
    def setUp(self):
        self.category = EmissionCategory.objects.create(name="Transportation")

    def test_create_emission_factor(self):
        factor = EmissionFactor.objects.create(
            category=self.category,
            name="Car",
            factor=0.21,
            unit="mile"
        )
        self.assertEqual(factor.factor, 0.21)
        self.assertEqual(factor.unit, "mile")


    def test_unique_names(self):
        EmissionFactor.objects.create(category=self.category, name="Car", factor=0.21, unit="mile")
        with self.assertRaises(Exception):
            EmissionFactor.objects.create(category=self.category, name="Car", factor=0.25, unit="mile")
