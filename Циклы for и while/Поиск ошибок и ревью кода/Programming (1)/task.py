s = 0
a = []
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        a.append(x)
if s == 0:
    print('NO')
else:
    print(s)
    print(max(a))