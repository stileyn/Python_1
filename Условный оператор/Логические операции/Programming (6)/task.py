# put your python code here
x1, y1, x2, y2 = [int(input()) for _ in range(4)]
if (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2):
    print('YES')
else:
    print('NO')