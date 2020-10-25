# На вход программе подается строка текста. Напишите программу,
# которая выводит на экран символ, который появляется наиболее часто.

string = input()
maximum, char = 0, ''
for i in string:
    if string.count(i) >= maximum:
        maximum = string.count(i)
        char = i
print(char)