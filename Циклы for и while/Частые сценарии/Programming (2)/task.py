# На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
# (1+1/2+1/3+…+1/n)−ln(n).

from math import log

n = int(input())
n1 = 0

for i in range(1, n + 1):
    n1 += 1 / i

print(n1 - log(n))

