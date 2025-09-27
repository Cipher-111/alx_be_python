FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

temp = int(input("Enter the temperature to convert: "))
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()


def convert_to_celsius(fahrenheit):
    ans = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return ans


def convert_to_fahrenheit(celsius):
    ans = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return ans


if degree == "C":

    print(convert_to_fahrenheit(temp))
elif degree == "F":
    print(convert_to_celsius(temp))
else:
    print("Invalid temperature. Please enter a numeric value.")
