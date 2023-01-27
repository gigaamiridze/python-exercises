class Bookshop():
    name =  None
    books = None
    choice = None
    quantity = None

    def __init__(self, b):
        self.books = b

    def sayHello(self):
        print('Welcome to the book store "Giga Books"')
        while not bool(self.name):
            self.name = input('Enter your name: ')
        print(f'Hello, {self.name.capitalize()}!')

    def showMenu(self):
        for item in enumerate(self.books.items(), start=1):
            (number, (name, price)) = item
            print(f'{number}. {name} - {price}.')

    def getChoice(self):
        self.choice = input('Specify the desired book: ').capitalize()
        while self.choice not in self.books:
            self.choice = input("Book name not found.\nPlease, select a book again: ").capitalize()

    def getQuantity(self):
        while True:
            self.quantity = input('Please enter a quantity: ')
            if not self.quantity.isnumeric():
                print('It does not reflect quantity.')
            else:
                break
            
    def calculate(self):
        return self.books.get(self.choice) * int(self.quantity)

    def showCalculate(self):
        print('You have to pay {} lari!'.format(self.calculate()))

    def payment(self):
        pay = input('Do you want to pay? (YES/NO) ').lower()
        while True:
            if pay == 'yes':
                print('Thank you for being our customer.')
                break

            elif pay == 'no':
                print('Goodbye. Good luck!')
                break

            else:
                print("Sorry, can't quite catch that.")
                pay = input('Do you want to pay? (YES/NO) ')

books_list = {
    'Grandmaster': 15,
    'Freedom': 22,
    'Ulises': 27
}

bookshop = Bookshop(books_list)
bookshop.sayHello()
bookshop.showMenu()
bookshop.getChoice()
bookshop.getQuantity()
bookshop.showCalculate()
bookshop.payment()
