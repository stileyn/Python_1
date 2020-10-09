# put your python code here
a, b, c = [int(input()) for _ in range(3)]
if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)
