# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def get_user_input():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            if unit not in ['C', 'F']:
                raise ValueError("Invalid temperature. Please enter a valid unit.")
            return temperature, unit
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    temperature, unit = get_user_input()

    if unit == 'F':
        converted_celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_celsius}°C")
    elif unit == 'C':
        converted_fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_fahrenheit}°F")