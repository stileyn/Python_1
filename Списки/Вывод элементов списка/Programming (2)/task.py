# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.

# num = [int(input()) for _ in range(int(input()))]
# num.remove(min(num))
# num.remove(max(num))
# print(* num, sep='\n')

l = []
for i in range(int(input())):
    l.append(int(input()))
for a in l:
    if a != min(l) and a != max(l):
        print(a)
