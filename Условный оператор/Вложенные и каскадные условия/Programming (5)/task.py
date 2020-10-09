# put your python code here
q, w, e = int(input()), int(input()), input()
if e == '/' and w == 0:
    print('На ноль делить нельзя!')
elif e == '/' and w != 0:
    print(q / w)
elif e == '+':
    print(q + w)
elif e == '-':
    print(q - w)
elif e == '*':
    print(q * w)
else:
    print('Неверная операция')
