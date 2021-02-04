"""Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел """
def fact2(n):
    factorial = 1
    if n % 2 == 0:
        count = 2
        while count <= n:
            factorial *= count
            count += 2
        return factorial
    else:
        count = 3
        while count <= n:
            factorial *= count
            count += 2
        return factorial
    
for count in range(5):
    number = int(input("enter the number: "))
    print(fact2(number))
