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

n=256
x=oct(n)#перевод в восмеричную систему
print(x)
print(int(x,8))#перевод обратно в десяятичную