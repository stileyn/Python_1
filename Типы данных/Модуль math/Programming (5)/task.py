# Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
# ax2+bx+c=0.

from math import *

a = float(input())
b = float(input())
c = float(input())

discr = b ** 2 - 4 * a * c

if discr > 0:
    x1 = (-b + sqrt(discr)) / (2 * a)
    x2 = (-b - sqrt(discr)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')
elif discr == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Нет корней")
