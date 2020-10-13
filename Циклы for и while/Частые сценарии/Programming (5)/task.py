# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

multiplication = 1

for i in range(10):
    n = int(input())
    if n != 0:
        multiplication *= n

print(multiplication)
