# Functions
# დავალება 1
# შექმენით ფუნქცია, რომელიც სამ ინდივიდუალურ რიცხვით არგუმენტს შორის უდიდესს დააბრუნებს.
# არ გამოიყენოთ პითონის ჩაშენებული ფუნქციები ან მონაცემთა სტრუქტურები (ლისტი, თაფლი...).

def custom_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


# დავალება 2
# შექმენით ფუნქცია, რომელსაც გადასცემთ ტექსტს (ლათინური ასოებით), ხოლო უკან დააბრუნებს Tuple-ს ([ხმოვნები], [თანხმოვნები]): 
# მაგალითი: vowel_consonant("abc") -> (["a"],["b","c"])

def vowel_consonant(str):
    vowels = []
    consonanst = []
    for v in str:
        if v in 'a,e,i,o,u':
            vowels.append(v)

    for c in str:
        if c not in 'a,e,i,o,u':
            consonanst.append(c)

    return f'{tuple([vowels])}, {tuple([consonanst])}'

word = input().lower()


# დავალება 3
# დაწერეთ ფუნქცია, რომელიც List-იდან ამოიღებს კონკრეტულ ელემენტს და დააბრუნებს ახალ List-ს მითითებული ელემენტის გარეშე.
# მაგალითი: custom_filter([1,2,3,4,4,4,4,4,5], 4) -> [1,2,3,5]

def custom_filter(lst, item):
    ordered = []
    for num in lst:
        if num != item:
            ordered.append(num)
    return ordered


# დავალება 4
# დაწერეთ ფუნქცია, რომელიც შეაჯამებს ყველა რიცხვს List-ში (for ციკლის მეშვეობით).
# მაგალითი: custom_sum([1,2,3,4,5]) -> 15

def custom_sum(lst):
    sum = 0
    for item in lst:
        sum += item
    return sum


# დავალება 5
# დაწერეთ ფუნქცია, რომელიც დააბრუნებს List-ის უნიკალურ ელემენტებს List-ად (type casting -ის მეშვეობით).
# მაგალითი: custom_unique_lst([1,2,2,3,4,5,3,4,5]) -> [1,2,3,4,5]

def custom_unique_lst(lst):
    lst = list(set(lst))
    return lst


# დავალება 6
# დაწერეთ ფუნქცია, რომელიც ჩადგმული ციკლის (Nested Loop) მეშვეობით დაგვიბრუნებს გამრავლების ტაბულას მითითებულ რიცხვამდე.
# მაგალითი: custom_mult_table(10) ფუნქციის შედეგი იქნება მიმაგრებულ ფაილში.
# https://www.w3schools.com/python/gloss_python_escape_characters.asp

def custom_mult_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f'| {i*j} ', end='')
        print('\n')


if __name__ == "__main__":
    print(custom_max(7, 5, 3))
    print(vowel_consonant(str=word))
    print(custom_filter([1, 2, 3, 4, 4, 4, 4, 4, 5], 4))
    print(custom_sum([1, 2, 3, 4, 5]))
    print(custom_unique_lst([1, 2, 2, 3, 4, 5, 3, 4, 5]))
    print(custom_mult_table(10))
