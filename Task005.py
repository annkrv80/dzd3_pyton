#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

import os
def clear(): return os.system('cls')


clear()
n = int(input('Введите размер ряда: '))
list = [0]


def Fib(n):
    if n in [1, 2]:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)


def NegaFib(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        f1, f2 = 1, -1
        for i in range(2, n):
            f1, f2 = f2, f1 - f2
        return f2


for e in range(1, n+1):
    list.append(Fib(e))
    list.insert(0, NegaFib(e))
print(list)
