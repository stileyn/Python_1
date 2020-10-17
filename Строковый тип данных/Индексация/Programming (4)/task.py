# На вход программе подаются три строки: имя, фамилия и отчество.
# Напишите программу, которая выводит инициалы человека.

surname, name, lastname = [input() for i in range(3)]

print(name[0], surname[0], lastname[0], sep='')