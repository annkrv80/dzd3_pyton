#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import os
from random import randint
def clear(): return os.system('cls')


clear()

list = [randint(-10, 10) for i in range(9)]
print(list)
list2 = []
for i in range((len(list)+1)//2):#к длинне списка прибавили +1 чтобы центральный эл. умножить сам на себя
    box = list[i]*list[-i-1]
    list2.append(box)
print(list2)
