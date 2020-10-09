# put your python code here
n, k = [int(input()) for _ in range(2)]
if n > k:
    print('NO')
elif k > n:
    print('YES')
else:
    print("Don't know")