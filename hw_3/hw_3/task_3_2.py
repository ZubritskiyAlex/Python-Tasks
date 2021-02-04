def choice_and_solution(a) -> str:
    if a > 50:
        solution = "Ресторан"
    elif 20 < a < 50:
        solution = "Кафе"
    else:
        solution = "Дом"
    return solution


a = input("Enter the number ")
if a.isdigit() == True:
    a = int(a)
    print(choice_and_solution(a))
else:
    print("ValueError")


a = input("Enter the number ")
try:
    a = int(a)
except ValueError:
    print(f"Строка {a} содержит недопустимые символы")
else:
    a = int(a)
    print(choice_and_solution(a))
