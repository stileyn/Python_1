# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

a, b, c = input(), input(), input()
x, y, z = len(a), len(b), len(c)
print(a if x < y and x < z else b if y < x and y < z else c)
print(a if x > y and x > z else b if y > x and y > z else c)