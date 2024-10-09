# Carbon emission factors (in kg CO2 per unit of energy)
EMISSION_FACTORS = {
    "electricity": 0.92,  # kg CO2 per kWh (varies by region, average is used here)
    "natural_gas": 2.05,  # kg CO2 per cubic meter
    "heating_oil": 2.52,  # kg CO2 per liter
    "propane": 1.51       # kg CO2 per liter (approximate value)
}

def calculate_emissions(electricity_kwh, natural_gas_m3, heating_oil_liters, propane_liters):
    # Calculate emissions for each energy source
    electricity_emissions = electricity_kwh * EMISSION_FACTORS["electricity"]
    natural_gas_emissions = natural_gas_m3 * EMISSION_FACTORS["natural_gas"]
    heating_oil_emissions = heating_oil_liters * EMISSION_FACTORS["heating_oil"]
    propane_emissions = propane_liters * EMISSION_FACTORS["propane"]
    
    # Calculate total emissions
    total_emissions = (electricity_emissions +
                       natural_gas_emissions +
                       heating_oil_emissions +
                       propane_emissions)
    
    return {
        "electricity_emissions_kg": electricity_emissions,
        "natural_gas_emissions_kg": natural_gas_emissions,
        "heating_oil_emissions_kg": heating_oil_emissions,
        "propane_emissions_kg": propane_emissions,
        "total_emissions_kg": total_emissions
    }

# Example usage
if __name__ == "__main__":
    # Sample input data for energy usage per day
    electricity_usage_kwh = float(input("Enter daily electricity usage in kWh: "))
    natural_gas_usage_m3 = float(input("Enter daily natural gas usage in cubic meters: "))
    heating_oil_usage_liters = float(input("Enter daily heating oil usage in liters: "))
    propane_usage_liters = float(input("Enter daily propane usage in liters: "))
    
    # Calculate daily emissions
    emissions = calculate_emissions(electricity_usage_kwh, natural_gas_usage_m3, heating_oil_usage_liters, propane_usage_liters)
    
    # Calculate emissions for different time periods
    daily_emissions = emissions['total_emissions_kg']
    weekly_emissions = daily_emissions * 7
    monthly_emissions = daily_emissions * 30  # Approximation
    yearly_emissions = daily_emissions * 365
    
    # Display results
    print("\nHousehold Carbon Emissions:")
    print(f"Daily emissions: {daily_emissions:.2f} kg CO2")
    print(f"Weekly emissions: {weekly_emissions:.2f} kg CO2")
    print(f"Monthly emissions: {monthly_emissions:.2f} kg CO2")
    print(f"Yearly emissions: {yearly_emissions:.2f} kg CO2")
    
    # Breakdown of emissions by source
    print("\nBreakdown of Daily Carbon Emissions by Source:")
    print(f"Electricity emissions: {emissions['electricity_emissions_kg']:.2f} kg CO2")
    print(f"Natural gas emissions: {emissions['natural_gas_emissions_kg']:.2f} kg CO2")
    print(f"Heating oil emissions: {emissions['heating_oil_emissions_kg']:.2f} kg CO2")
    print(f"Propane emissions: {emissions['propane_emissions_kg']:.2f} kg CO2")
