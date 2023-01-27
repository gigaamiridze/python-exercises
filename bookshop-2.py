print('Welcome to the book store "Giga Books"')

name = input('Enter your name: ')
print(f'Hello, {name.capitalize()}!')

books = {
    'Grandmaster': 15,
    'Freedom': 22,
    'Ulises': 27
}

print('List of books today:')
for item in enumerate(books.items(), start=1):
    (number, (name, price)) = item
    print(f'{number}. {name} - {price}')

choose_book = input('Specify the desired book: ').capitalize()
while choose_book not in books.keys():
    choose_book = input("Book name not found.\nPlease, select a book again: ").capitalize()

quantity = int(input('Please enter a quantity: '))
books = tuple(books.items())

if choose_book == 'Grandmaster':
    full_price = quantity * books[0][1]
    print(f'You have to pay {full_price} lari!')

elif choose_book == 'Freedom':
    full_price = quantity * books[1][1]
    print(f'You have to pay {full_price} lari!')

elif choose_book == 'Ulises':
    full_price = quantity * books[2][1]
    print(f'You have to pay {full_price} lari!')

pay = input('Do you want to pay? (YES/NO) ').lower()

condition = True
while condition:
    if pay == 'yes':
        print('Thank you for being our customer.')
        condition = False

    elif pay == 'no':
        print('Goodbye. Good luck!')
        condition = False

    else:
        print("Sorry, can't quite catch that.")
        pay = input('Do you want to pay? (YES/NO) ')
