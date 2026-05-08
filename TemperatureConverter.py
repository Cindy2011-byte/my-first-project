temperature = float(input('Enter a temperature: '))
unit = input('Is the unit in Celsius or Fahrenheit (C/F)?: ')

if unit == 'C':
    result = temperature * 9/5 + 32
    print(f'The temperature is {result:.1f}°F')
elif unit == 'F':
    result = (temperature - 32) * 5/9
    print(f'The temperature is {result:.1f}°C')
else:
    print(f'{unit} is not a valid unit')