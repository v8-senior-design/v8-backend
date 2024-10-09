# Average carbon footprint in kg CO₂e per kg of food product
# Carbon footprint values are based on data from Poore, J., & Nemecek, T. (2018).
# Reducing food’s environmental impacts through producers and consumers. Science, 360(6392), 987-992.
carbon_footprint_per_kg = {
    'beef': 60,       # kg CO₂e per kg
    'lamb': 24,       # kg CO₂e per kg
    'chicken': 6,     # kg CO₂e per kg
    'pork': 7,        # kg CO₂e per kg
    'fish': 5,        # kg CO₂e per kg
    'dairy': 3,       # kg CO₂e per kg
    'eggs': 2.5,      # kg CO₂e per kg
    'vegetables': 2,  # kg CO₂e per kg
    'fruits': 1.5,    # kg CO₂e per kg
    'grains': 1.3,    # kg CO₂e per kg
    'legumes': 0.9,   # kg CO₂e per kg
    'nuts': 2.3       # kg CO₂e per kg
}

# Conversions 
lbs_to_kg = 0.453592  # 1 pound (lb) = 0.453592 kilograms (kg)
kg_to_lbs = 2.20462   # 1 kilogram (kg) = 2.20462 pounds (lbs)

# Function to validate unit input from user (kg or lbs)
def get_unit_input(prompt):
    while True:
        unit = input(prompt).strip().lower()
        if unit in ['kg', 'lbs', 'pounds', 'kilograms']:
            return 'lbs' if unit == 'pounds' else 'kg' if unit == 'kilograms' else unit
        else:
            print("\nInvalid input! Please enter 'kg' for kilograms or 'lbs' for pounds.\n")

# Ask user for input unit preference (kg or lbs)
unit_choice = get_unit_input("Would you like to input your consumption in kilograms (kg) or pounds (lbs)? ")

# Initialize consumption dictionary
consumption = {}

# Input consumption based on the unit choice
if unit_choice == 'lbs':
    print("Estimate the amount of each food product you consume per week (in pounds):")
    for food in carbon_footprint_per_kg:
        while True:
            try:
                amount = float(input(f"{food.capitalize()} (in lbs): "))
                # Convert pounds to kilograms
                consumption[food] = amount * lbs_to_kg
                break
            except ValueError:
                print("Please enter a valid number.")
else:
    print("Estimate the amount of each food product you consume per week (in kilograms):")
    for food in carbon_footprint_per_kg:
        while True:
            try:
                amount = float(input(f"{food.capitalize()} (in kg): "))
                consumption[food] = amount
                break
            except ValueError:
                print("Please enter a valid number.")

# Calculate the total carbon footprint per week (in kg CO₂e)
total_weekly_footprint_kg = sum(
    carbon_footprint_per_kg[food] * consumption[food]
    for food in consumption
)

# If input was in pounds, convert the results to pounds
if unit_choice == 'lbs':
    total_weekly_footprint = total_weekly_footprint_kg * kg_to_lbs
    total_daily_footprint = (total_weekly_footprint_kg / 7) * kg_to_lbs
    total_monthly_footprint = (total_weekly_footprint_kg * 4.345) * kg_to_lbs  # Approx. weeks per month
    total_yearly_footprint = (total_weekly_footprint_kg * 52) * kg_to_lbs  # 52 weeks in a year
    unit = "lbs"
else:
    total_weekly_footprint = total_weekly_footprint_kg
    total_daily_footprint = total_weekly_footprint_kg / 7
    total_monthly_footprint = total_weekly_footprint_kg * 4.345  # Approx. weeks per month
    total_yearly_footprint = total_weekly_footprint_kg * 52  # 52 weeks in a year
    unit = "kg"

# Display results in the same unit as the input
print(f"\nYour carbon footprint from your provided diet is:")
print(f" - Daily: {total_daily_footprint:.2f} {unit} CO₂e")
print(f" - Weekly: {total_weekly_footprint:.2f} {unit} CO₂e")
print(f" - Monthly: {total_monthly_footprint:.2f} {unit} CO₂e")
print(f" - Yearly: {total_yearly_footprint:.2f} {unit} CO₂e")

# Note: CO₂e = tonnes of carbon dioxide equivalents

#For running in CMD
input("\nPress 'Enter' to close the window...")

