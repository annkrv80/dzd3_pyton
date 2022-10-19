#Задайте список из нескольких чисел.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import os
from random import randint
def clear(): return os.system('cls')


clear()

list = [randint(0, 10) for i in range(5)]
print(list)
print(sum(list[1::2])) #срез списка от 1 до конца с шагом 2