# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.

from math import *

radius = float(input())

print(pi * radius ** 2, 2 * pi * radius, sep='\n')
