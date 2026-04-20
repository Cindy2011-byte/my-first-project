item1 = 'apple'
item2 = 'banana'
price1 = 1.22
price2 = 2.00
quantity1 = int(input(f'How many {item1} do you want to buy? '))
quantity2 = int(input(f'How many {item2} do you want to buy? '))
total_price = price1 * quantity1 + price2 * quantity2
print(f'The total price is ${total_price}')