# put your python code here
a, b, c = [int(input()) for _ in range(3)]
if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')