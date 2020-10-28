# На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется
# список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

s = input()
user_list = [int(number) for number in s.split()]

a, b = user_list.index(min(user_list)), user_list.index(max(user_list))
user_list[a], user_list[b] = user_list[b], user_list[a]
print(*user_list)

