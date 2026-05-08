weight = float(input('Enter your weight: '))
unit = input('Is your weight in kilograms or pounds (kg or lbs)?: ')

if unit == 'kg':
    result = weight * 2.2
    print(f'The weight in pounds is {result:.1f}lbs')
elif unit == 'lbs':
    result = weight / 2.2
    print(f'The weight in kilograms is {result:.1f}kg')
else:
    print(f'{unit} is not a valid unit')