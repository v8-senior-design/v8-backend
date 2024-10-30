from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Provision Model
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


# Provision Model
class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='category_subcategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class EmissionCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class EmissionFactor(models.Model):
    category = models.ForeignKey(EmissionCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    factor = models.FloatField(help_text="Emission factor in kg CO2e per unit")
    unit = models.CharField(max_length=50, help_text="Unit of measurement (e.g., kWh, gallon, serving)")

    class Meta:
        unique_together = ('category', 'name')

    def __str__(self):
        return f"{self.name} ({self.factor} kg CO2e per {self.unit})"


class Emission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.ForeignKey(EmissionCategory, on_delete=models.CASCADE)
    emission_factor = models.ForeignKey(EmissionFactor, on_delete=models.CASCADE)
    quantity = models.FloatField(help_text="Amount of activity (e.g., kWh, miles, servings)")
    total_emissions_kg = models.FloatField(editable=False, default=0)

    def calculate_emissions(self):
        return self.quantity * self.emission_factor.factor

    def save(self, *args, **kwargs):
        self.total_emissions_kg = self.calculate_emissions()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.emission_factor.name} on {self.date} for {self.user.email}"
