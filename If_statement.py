num = int(input('Enter a number: '))

if num / 2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')


numbers = float(input('Enter a number: '))

if numbers < 0:
    print('The number is negative.')
elif numbers == 0:
    print('The number is zero.')
else:
    print('The number is positive.')


age = int(input('Enter your age: '))

if age >= 40:
    print('Sorry, you are too old to get drafted.')
elif age >= 18:
    print('Congratulations, you are drafted to war!')
else:
    print('Sorry, you are too young to get drafted.')

