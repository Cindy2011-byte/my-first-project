operator = input('Choose an operator [+ - * /]: ')
num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(round(num1 / num2,2))
else:
    print(f'{operator} is not a valid operator')