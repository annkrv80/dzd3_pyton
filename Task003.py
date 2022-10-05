#Задайте список из вещественных чисел. Напишите программу,
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import os
import sys
def clear(): return os.system('cls')


clear()
list = [7.3, 8.2, 1.01, 5, 6.4]
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
