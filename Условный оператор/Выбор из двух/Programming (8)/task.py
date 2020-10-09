# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

q, w, e = int(input()), int(input()), int(input())
d = 0
if q > 0:
    d += q
if w > 0:
    d += w
if e > 0:
    d += e
if d > 0:
    print(d)
else:
    print(0)