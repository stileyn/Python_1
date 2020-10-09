# Напишите программу, вычисляющее значение ⌈x⌉+⌊x⌋ по заданному вещественному числу x.

from math import *

x = float(input())

print(ceil(x) + floor(x))
