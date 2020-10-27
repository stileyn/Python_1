# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая
# для каждого из введенного числа x выводит значение функции f(x)=x2+2x+1, каждое на отдельной строке.

# n = int(input())
# b = []
# for _ in range(n):
#     n = int(input())
#     b.append(n)
#
# print(* b, '', *[x + 1 ** 2 for x in b], sep='\n')

numbers = [int(input()) for _ in range(int(input()))]
print(*numbers, '',*[(x + 1) ** 2 for x in numbers], sep='\n')
