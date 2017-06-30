#Write a program which propmts the user for a Celsius temperature, convert the
#temperature to Fahrenheit, and print out the converted temperature

# Get input
tempCelsius = input('Give a value in Celsius: ')

# Convert to Fahrenheit
tempFahr = float(tempCelsius) * (9.0 / 5.0) + 32

# Print out result
print('In Fahrenheit scale = ' + str(tempFahr))
