FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
	return(round(fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR,2))


def convert_to_fahrenheit(celsius):
	return(round(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR,2))


while True:
    try:
        temperature = float(input("Enter the temperature to convert: "))
        break  
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

while True:
	unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if unit.upper() == 'F' or unit.upper() == 'C':
		break
	print("invalid value")

if unit.upper() == 'C':
	print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")	

elif unit.upper() == 'F':
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
