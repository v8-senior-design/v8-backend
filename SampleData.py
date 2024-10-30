# Run in Django shell: python manage.py shell

from django.contrib.auth import get_user_model
from calc.models import EmissionCategory, EmissionFactor, Emission
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

# Create or get users
users_data = [
    {'email': 'filip@gmail.com'},
    {'email': 'martin@gmail.com'},
    {'email': 'alice@example.com'},
    {'email': 'bob@example.com'},
]

for user_data in users_data:
    user, created = User.objects.get_or_create(
        email=user_data['email'],
        defaults={'email': user_data['email']}
    )
    if created:
        user.set_password('your_secure_password')  # Replace with a secure password
        user.save()

# Fetch users
filip = User.objects.get(email='filip@gmail.com')
martin = User.objects.get(email='martin@gmail.com')
alice = User.objects.get(email='alice@example.com')
bob = User.objects.get(email='bob@example.com')

# Create Emission Categories
categories = ['Household', 'Transportation', 'Meal', 'Drink']
for category_name in categories:
    EmissionCategory.objects.get_or_create(name=category_name)

# Fetch categories
household_category = EmissionCategory.objects.get(name='Household')
transportation_category = EmissionCategory.objects.get(name='Transportation')
meal_category = EmissionCategory.objects.get(name='Meal')
drink_category = EmissionCategory.objects.get(name='Drink')

# Create Emission Factors
# Household Factors
household_factors = [
    {'name': 'Electricity', 'factor': 0.92, 'unit': 'kWh'},
    {'name': 'Natural Gas', 'factor': 2.05, 'unit': 'cubic meter'},
    {'name': 'Heating Oil', 'factor': 2.52, 'unit': 'liter'},
    {'name': 'Propane', 'factor': 1.51, 'unit': 'liter'},
]

for factor_data in household_factors:
    EmissionFactor.objects.get_or_create(
        category=household_category,
        name=factor_data['name'],
        defaults={'factor': factor_data['factor'], 'unit': factor_data['unit']}
    )

# Transportation Factors
transportation_factors = [
    {'name': 'Regular Gasoline', 'factor': 8.89, 'unit': 'gallon'},
    {'name': 'Midgrade Gasoline', 'factor': 8.92, 'unit': 'gallon'},
    {'name': 'Premium Gasoline', 'factor': 8.94, 'unit': 'gallon'},
    {'name': 'Diesel Fuel', 'factor': 10.21, 'unit': 'gallon'},
]

for factor_data in transportation_factors:
    EmissionFactor.objects.get_or_create(
        category=transportation_category,
        name=factor_data['name'],
        defaults={'factor': factor_data['factor'], 'unit': factor_data['unit']}
    )

# Meal Factors
meal_factors = [
    {'name': 'Omnivore Meal', 'factor': 2.5, 'unit': 'serving'},
    {'name': 'Vegetarian Meal', 'factor': 1.7, 'unit': 'serving'},
    {'name': 'Vegan Meal', 'factor': 1.5, 'unit': 'serving'},
]

for factor_data in meal_factors:
    EmissionFactor.objects.get_or_create(
        category=meal_category,
        name=factor_data['name'],
        defaults={'factor': factor_data['factor'], 'unit': factor_data['unit']}
    )

# Drink Factors
drink_factors = [
    {'name': 'Alcohol', 'factor': 0.8, 'unit': 'serving'},
    {'name': 'Coffee', 'factor': 0.2, 'unit': 'cup'},
    {'name': 'Milk', 'factor': 0.6, 'unit': 'cup'},
    {'name': 'Vegan Milk', 'factor': 0.3, 'unit': 'cup'},
    {'name': 'Soft Drink', 'factor': 0.4, 'unit': 'cup'},
    {'name': 'Water', 'factor': 0.05, 'unit': 'cup'},
]

for factor_data in drink_factors:
    EmissionFactor.objects.get_or_create(
        category=drink_category,
        name=factor_data['name'],
        defaults={'factor': factor_data['factor'], 'unit': factor_data['unit']}
    )

# Fetch Emission Factors (for use in emissions)
electricity_factor = EmissionFactor.objects.get(category=household_category, name='Electricity')
natural_gas_factor = EmissionFactor.objects.get(category=household_category, name='Natural Gas')
heating_oil_factor = EmissionFactor.objects.get(category=household_category, name='Heating Oil')
propane_factor = EmissionFactor.objects.get(category=household_category, name='Propane')

regular_gasoline_factor = EmissionFactor.objects.get(category=transportation_category, name='Regular Gasoline')
midgrade_gasoline_factor = EmissionFactor.objects.get(category=transportation_category, name='Midgrade Gasoline')
premium_gasoline_factor = EmissionFactor.objects.get(category=transportation_category, name='Premium Gasoline')
diesel_factor = EmissionFactor.objects.get(category=transportation_category, name='Diesel Fuel')

omnivore_meal_factor = EmissionFactor.objects.get(category=meal_category, name='Omnivore Meal')
vegetarian_meal_factor = EmissionFactor.objects.get(category=meal_category, name='Vegetarian Meal')
vegan_meal_factor = EmissionFactor.objects.get(category=meal_category, name='Vegan Meal')

alcohol_factor = EmissionFactor.objects.get(category=drink_category, name='Alcohol')
coffee_factor = EmissionFactor.objects.get(category=drink_category, name='Coffee')
milk_factor = EmissionFactor.objects.get(category=drink_category, name='Milk')
vegan_milk_factor = EmissionFactor.objects.get(category=drink_category, name='Vegan Milk')
soft_drink_factor = EmissionFactor.objects.get(category=drink_category, name='Soft Drink')
water_factor = EmissionFactor.objects.get(category=drink_category, name='Water')

# Create Sample Emissions with different dates and quantities
today = timezone.now().date()
dates = [today - timedelta(days=i) for i in range(5)]  # Last 5 days

# Sample emissions for each user
emissions_data = [
    # Filip's emissions
    {
        'user': filip,
        'emissions': [
            {'date': dates[0], 'category': household_category, 'emission_factor': electricity_factor, 'quantity': 20},
            {'date': dates[1], 'category': transportation_category, 'emission_factor': regular_gasoline_factor, 'quantity': 6},
            {'date': dates[2], 'category': meal_category, 'emission_factor': omnivore_meal_factor, 'quantity': 2},
            {'date': dates[3], 'category': drink_category, 'emission_factor': coffee_factor, 'quantity': 4},
        ],
    },
    # Martin's emissions
    {
        'user': martin,
        'emissions': [
            {'date': dates[0], 'category': household_category, 'emission_factor': natural_gas_factor, 'quantity': 12},
            {'date': dates[1], 'category': transportation_category, 'emission_factor': diesel_factor, 'quantity': 5},
            {'date': dates[2], 'category': meal_category, 'emission_factor': vegetarian_meal_factor, 'quantity': 3},
            {'date': dates[3], 'category': drink_category, 'emission_factor': milk_factor, 'quantity': 2},
        ],
    },
    # Alice's emissions
    {
        'user': alice,
        'emissions': [
            {'date': dates[0], 'category': household_category, 'emission_factor': propane_factor, 'quantity': 15},
            {'date': dates[1], 'category': transportation_category, 'emission_factor': midgrade_gasoline_factor, 'quantity': 4},
            {'date': dates[2], 'category': meal_category, 'emission_factor': vegan_meal_factor, 'quantity': 3},
            {'date': dates[3], 'category': drink_category, 'emission_factor': vegan_milk_factor, 'quantity': 2},
        ],
    },
    # Bob's emissions
    {
        'user': bob,
        'emissions': [
            {'date': dates[0], 'category': household_category, 'emission_factor': heating_oil_factor, 'quantity': 18},
            {'date': dates[1], 'category': transportation_category, 'emission_factor': premium_gasoline_factor, 'quantity': 7},
            {'date': dates[2], 'category': meal_category, 'emission_factor': omnivore_meal_factor, 'quantity': 1},
            {'date': dates[3], 'category': drink_category, 'emission_factor': alcohol_factor, 'quantity': 3},
        ],
    },
]

# Create emissions
for user_data in emissions_data:
    user = user_data['user']
    for emission in user_data['emissions']:
        Emission.objects.create(
            user=user,
            date=emission['date'],
            category=emission['category'],
            emission_factor=emission['emission_factor'],
            quantity=emission['quantity']
        )

print("Sample data insertion complete.")
