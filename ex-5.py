# დავალება 1
# დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს Dict-ს და დაბეჭდავს პროდუქტის ინდექსს, პროდუქტს და ფასს, ასეთი ფორმატით: "{index}. {product} - {price}"
products = {
    "brown": 9.15,
    "bounty": 11.5,
    "cheesecake": 15.99
}

def print_dict(products):
    for item in enumerate(products.items(), start=1):
        (index, (product, price)) = item
        print(f'{index}. {product} - {price}')


# დავალება 2
# დაწერეთ ლამბდა ფუნქცია, რომელიც დააბრუნებს რიცხვის კუბს.
# მაგალითი: cube(2) -> 8
cube = lambda x: x ** 3


# დავალება 3
# დაწერეთ ფუნქცია, რომელიც მიიღებს პარამეტრად ერთ რიცხვს და დააბრუნებს მნიშვნელობებს even/odd (String-ად) რიცხვის შესაბამისად.
# მაგალითი: singleEvenOdd(3) -> 'odd', singleEvenOdd(2) -> 'even'
def singleEvenOdd(x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'


# დავალება 4 (დამოკიდებულია დავალება 3 -ზე)
# დაწერეთ while ციკლი, რომელიც მიიღებს მთელ რიცხვს და ყოველ იტერაციაზე დააკლებს მნიშვნელობას (და გაჩერდება თუ მიაღწევს ნულს) და List-ში შეინახავს tuple წყვილებს, სადაც პირველი იქნება რიცხვი, მეორე კი სიტყვა even/odd. 
# მაგალითი: evenOdd(5) -> [(5, 'odd'), (4, 'even'), (3, 'odd'), (2, 'even'), (1, 'odd')]
def evenOdd(n):
    num = []
    while n != 0:
        par = (n, singleEvenOdd(n))
        num.append(par)
        n = n - 1
    return num


# დავალება 5
# დაწერეთ list comprehension-ის მეშვეობით ფუნქცია, რომელიც მასივის ყოველ ელემენტს აახარიხებს მეორე ხარისხში და დაგვიბრუნებს ახარისხებულ ლისტს. 
# მაგალითი: powerList([1, 2, 3]) -> [1, 4, 9] 
def powerList(lst):
    result = [item**2 for item in lst]
    return result


# დავალება 6
# დაწერეთ list comprehension-ის მეშვეობით ფუნქცია, რომელიც ორი ლისტის ელემენტებს გააერთიანებს წინადადებებად და დაგვიბრუნებს გაერთიანებულ სთრინგებს ლისტში. 
# მაგალითი: string_mix(["John,", "Jane,"], ["Hello!", "How are you?"]) -> ['John, Hello!', 'John, How are you?', 'Jane, Hello!', 'Jane, How are you?']
def string_mix(lst1, lst2):
    result = [item1 + item2 for item1 in lst1 for item2 in lst2]
    return result

if __name__ == "__main__":
    print_dict(products)
    print(cube(2))
    print(singleEvenOdd(5))
    print(powerList([1, 2, 3]))
    print(string_mix(["John,", "Jane,"], ["Hello!", "How are you?"]))
