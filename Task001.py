#Задайте список из нескольких чисел.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import os
from random import randint
def clear(): return os.system('cls')


clear()

list = [randint(-10, 10) for i in range(10)]
print(list)
sum = 0
for i in range(1, len(list), 2):
    sum += list[i]
print(sum)
