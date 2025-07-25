# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("🌡️ Temperature Conversion Tool")
    
    temp_input = input("Enter the temperature (e.g. 37.5): ").strip()
    unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().lower()

    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    if unit == 'c':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted:.2f}°F")
    elif unit == 'f':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
