# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.


def sum_of_digits(n):
    summa = 0
    while n > 0:
        a = n % 10
        summa += a
        n = n // 10
    return summa


def number_of_digits(n):
    total = 0
    while n > 0:
        total += 1
        n = n // 10
    return total


def composition_of_digits(n):
    composition = 1
    while n > 0:
        a = n % 10
        composition *= a
        n = n // 10
    return composition


def average_of_digits(n):
    return sum_of_digits(n) / number_of_digits(n)


def one_number(n):
    a = []
    while n > 0:
        a.append(n % 10)
        n = n // 10
    a.reverse()
    return a[0]


def sum_one_and_last(n):
    a = []
    while n > 0:
        a.append(n % 10)
        n = n // 10
    a.reverse()
    return a[0] + a[-1]


n = int(input())
print(sum_of_digits(n),
      number_of_digits(n),
      composition_of_digits(n),
      average_of_digits(n),
      one_number(n),
      sum_one_and_last(n),
      sep='\n')
