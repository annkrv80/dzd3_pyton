#Задайте список из вещественных чисел. Напишите программу,
#которая найдёт разницу между максимальным и минимальным значением дробной части элементkов.
import abc


spisok=[1.1,3.2,5,6.01,3.5]
sp_frac=[abs(i-int(i)) for i in spisok if int(i)!=i]#int(i)!=i исключить число без дробной части abs модуль числа
print(sp_frac)
print(max(sp_frac)-min(sp_frac))