"""Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)"""
def check_palindrom (my_word:str)->str:
    if my_word == my_word[::-1]:
        solution = "palindrom"
    else:
        solution ="not palindrom "
    return solution

for i in range(3):
    word = input("enter the word: ")
    print(check_palindrom(word))
