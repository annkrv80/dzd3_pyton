#Задайте список из вещественных чисел. Напишите программу,
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import os
import random
import sys
def clear(): return os.system('cls')


clear()
list = [round(random.uniform(0.01, 20), 2) for x in range(6)]
print(list)
list2 = []
for i in range(len(list)):
   c = round((list[i]-int(list[i])), 2)
   if c != 0:
    list2.append(c)
print(list2)
max = 0
min = list2[0]
for i in range(len(list2)):
   if list2[i] > max:
    max = list2[i]
   if list2[i] < min:
    min = list2[i]
print(max-min)
