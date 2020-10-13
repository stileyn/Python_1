# Дано натуральное число n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

def two_number(n):
    # a = []
    # while n > 0:
    #     a.insert(0, n % 10)
    #     n = n // 10
    # return a[1]
    return n[1]


n = (input())
print(two_number(n))
