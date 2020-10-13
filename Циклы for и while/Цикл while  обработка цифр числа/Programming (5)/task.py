# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

def all_the_same(elements):
    return len(elements) < 1 or len(elements) == elements.count(elements[0])

elemetns = input()
print('YES' if all_the_same(elemetns) == True else 'NO')