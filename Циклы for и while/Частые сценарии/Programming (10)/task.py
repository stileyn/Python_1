# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.

fib1 = fib2 = 1

n = int(input())

if n < 2:
    print(fib1, end=' ')
    quit()

print(fib1, end=' ')
print(fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

