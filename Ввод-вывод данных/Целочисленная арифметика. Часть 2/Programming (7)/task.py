# Дано трехзначное число abc¯¯¯¯¯¯¯, в котором все цифры различны. Напишите программу, которая выводит шесть чисел,
# образованных при перестановке цифр заданного числа.

abc = input()
print(abc)
print(abc[0], abc[2], abc[1], sep='')
print(abc[1], abc[0], abc[2], sep='')
print(abc[1], abc[2], abc[0], sep='')
print(abc[2], abc[0], abc[1], sep='')
print(abc[2], abc[1], abc[0], sep='')

