# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу,
# которая выводит k-ую букву из введенных строк на одной строке без пробелов.

n = int(input())
a = []
b = ''
for _ in range(n):
    n = input()
    a.append(n)

k = int(input())

for i in range(len(a)):
    if len(a[i]) >= k:
        b += a[i][k - 1]
print(b)