# На вход программе подается натуральное число n. Напишите программу, выводящую графическое изображение делимости
# чисел от 1 до n включительно. В каждой строке надо напечатать очередное число и столько символов «+»,
# сколько делителей у этого числа.

n = int(input())

for i in range(1, n + 1):
    total_divisors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total_divisors += 1
    print(i, total_divisors * '+', sep='')