a = input("Enter the number: ")
if a.isdigit() == True:
    a = int(a)
    if a % 1000 == 0:
        print("millenium")
else:
    print("ValueError")


a = input("Enter the number: ")
try:
    a = int(a)
    if a % 1000 == 0:
        print("millenium")
except ValueError:
    print(f"Строка {a} содержит недопустимые символы")
