#global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#function declaration F to C
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

#function declaration C to F
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

#take user input
temperature = float(input("Enter the temperature to convert: "))
conversion_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

match conversion_unit:
    case "c" if temperature.is_integer() or (isinstance(temperature, float) == True):
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    case "f" if temperature.is_integer() or (isinstance(temperature, float) == True):
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
    case _:
        print("Invalid temperature. Please enter a numeric value.")