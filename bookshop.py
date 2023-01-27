# A code for the consumer that summarizes the price of the books purchased
print('Welcome to the book store "Giga Books"')

name = input('Enter your name: ')
print(f'Hello, {name}!')

books = {
    'Grandmaster': 15,
    'Freedom': 22,
    'Ulises': 27
}

books_list = []
full_price = 0

print('List of books today:')
for i in books:
    print(i)
    books_list.append(books[i])

choose_book = input('Specify the desired book: ')
quantity = int(input('Please enter a quantity: '))

if choose_book == 'Grandmaster':
    full_price += quantity * books_list[0]
    print(f'You have to pay {full_price} lari!')
    print('Thank you for being our customer')

elif choose_book == 'Freedom':
    full_price += quantity * books_list[1]
    print(f'You have to pay {full_price} lari!')
    print('Thank you for being our customer')

elif choose_book == 'Ulises':
    full_price += quantity * books_list[2]
    print(f'You have to pay {full_price} lari!')
    print('Thank you for being our customer')
