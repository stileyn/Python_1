# На вход программе подается два натуральных числа a и b (a<b). Напишите программу, которая находит натуральное число
# из отрезка [a;b] с максимальной суммой делителей.

a, b = int(input()), int(input())
max_summa, final_number = 0, 0
for i in range(a, b + 1):
    summa = 0
    for j in range(1, i + 1):
        if i % j == 0:
            summa += j
        if max_summa <= summa:
            max_summa = summa
            final_number = j
print(final_number, max_summa)