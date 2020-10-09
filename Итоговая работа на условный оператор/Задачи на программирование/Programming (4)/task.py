# put your python code here
n = int(input())

if 2 <= n <= 5 and n % 2 == 0:
    print('NO')
elif 6 <= n <= 20 and n % 2 == 0:
    print('YES')
elif n % 2 == 0 and n > 20:
    print('NO')
elif n % 2 != 0:
    print('YES')