# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

from math import *

a, b = float(input()), float(input())

print((a + b) / 2)
print(sqrt(a * b))
print(2 * a * b / (a + b))
print(sqrt((a * a + b * b) / 2))
