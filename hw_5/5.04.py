#Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.
s = 0
i = 1
N = int(input())
while i <= N:
    s += 1/i
    i += 1
print(s)