# Программа должна вывести одно число – значение тригонометрического выражения.

from math import *

x = float(input())

print(sin(radians(x)) + cos(radians(x)) + tan(radians(x)) ** 2)