def only_letters(string):
    return all(letter.isalpha() for letter in string)

stroka = input("Enter the str: ")
a = len(stroka)
middle = int(a / 2)
if only_letters(stroka):
    if a % 2 == 0:
        print(stroka[middle-1])
    elif stroka[0] == stroka[middle]:
        print(stroka[1:a-1])
    else:
        print(stroka[middle])
else:
    print(f"Строка {stroka} содержит не только буквы!")

