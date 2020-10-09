# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

a, b, c = [int(input()) for _ in range(3)]
if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)
