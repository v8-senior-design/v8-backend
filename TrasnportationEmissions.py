def gallons_used(drive_distance, miles_pg):
    """Calculate the gallons used based on distance traveled and MPG."""
    return drive_distance / miles_pg


def calculate_emissions(fuel_type, gallons):
    """Calculate the carbon footprint based on fuel type and gallons used."""
    return fuel_type * gallons


def main():
    # Fuel type emission factors (in kg CO2 per gallon)
    REGULAR = 8.89
    MIDGRADE = 8.92
    PREMIUM = 8.94
    DIESEL = 10.21

    # Input for distance traveled and MPG
    drive_distance = float(input("Distance traveled by your vehicle (miles): "))
    miles_pg = float(input("Average miles per gallon (MPG) of your vehicle: "))
    
    # Menu to choose fuel type
    print("\na) Regular Gasoline (87 octane)")
    print("b) Midgrade Gasoline (89 octane)")
    print("c) Premium Gasoline (91 - 93 octane)")
    print("d) Diesel Fuel")
    print("e) Exit")

    # Input for fuel type
    option = input("\nSelect an option for the fuel type used: ")

    # Calculations based on fuel type selection
    if option == 'a':
        gallons = gallons_used(drive_distance, miles_pg)
        emissions_result = calculate_emissions(REGULAR, gallons)
        print(f"Carbon footprint: {emissions_result:.2f} kg CO2")

    elif option == 'b':
        gallons = gallons_used(drive_distance, miles_pg)
        emissions_result = calculate_emissions(MIDGRADE, gallons)
        print(f"Carbon footprint: {emissions_result:.2f} kg CO2")

    elif option == 'c':
        gallons = gallons_used(drive_distance, miles_pg)
        emissions_result = calculate_emissions(PREMIUM, gallons)
        print(f"Carbon footprint: {emissions_result:.2f} kg CO2")

    elif option == 'd':
        gallons = gallons_used(drive_distance, miles_pg)
        emissions_result = calculate_emissions(DIESEL, gallons)
        print(f"Carbon footprint: {emissions_result:.2f} kg CO2")

    elif option == 'e':
        print("Terminated")
        print("\n----------------------------------------------------------\n")

    else:
        print("Invalid option. Please try again.")
        print("\n----------------------------------------------------------\n")


# Run the program
if __name__ == "__main__":
    main()
