#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
import os
from tkinter import W
def clear(): return os.system('cls')


clear()

number = int(input('Введите число:'))
numBin = ' '
while number > 0:
    numBin = str(number % 2)+numBin
    number = number//2
print(numBin)
