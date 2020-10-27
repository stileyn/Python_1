# Напишите программу, выводящую следующий список:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
l = []
for i in range(97, 123):
    l.append(chr(i) * (i - 96))
print(l)