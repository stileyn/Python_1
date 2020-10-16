n = int(input())
a = -1
while n > 0:
    a = n % 10
    n //= 10
print(a)