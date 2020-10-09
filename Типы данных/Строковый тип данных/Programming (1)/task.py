# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
#
# «Hello [введенное имя] [введенная фамилия]! You just delved into Python».

firstname, lastname = input(), input()

print(f"Hello {firstname} {lastname}! You just delved into Python")