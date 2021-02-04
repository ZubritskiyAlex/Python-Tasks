"""Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
вещественные, ε > 0), находящую приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
Sin1 найти приближенное значение синуса для данного x при шести данных
ε ."""

def Sin1(x,epsilon: float) -> float:
    """The function calculate sin(x, e)
    :parameter x: Value in sin(x)
    :parameter ep: Accuracy of calculate
    :return: Result of sin(x, e)
    """

    start_sum = x
    start_mult_x = x
    start_znam = 1
    value = start_mult_x / start_znam
    counter = 1
    while abs(value) > epsilon:
        start_mult_x *= -x ** 2
        start_znam *= 2 * counter * (2 * counter + 1)
        value = start_mult_x / start_znam
        start_sum += value
        counter += 1
    return start_sum


while True:
    x = float(input('Enter value of x : '))
    for i in range(6):
        epsilon = float(input("Enter value of epsilon :"))
        if x == 0:
            print("answer is 0 ")
        elif epsilon > 0:
            print(f"Value of sin(x,e): {Sin1(x, epsilon)}")
        else:
            print('Bad input, eps > 0')
