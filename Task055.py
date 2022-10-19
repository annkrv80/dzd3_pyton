#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
import os
clear=lambda:os.system ('cls')
clear()
n = int(input('Введите размер ряда: '))

fib=[0,1]

for i in range(2,n+1):
    fib.append(fib[-1]+fib[-2])
for i in range(n):
    #fib=[fib[1]-fib[0]]+fib
    fib.insert(0,fib[1]-fib[0])

print(fib)