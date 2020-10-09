# Напишите программу, которая упорядочивает три числа от большего к меньшему.

number1, number2, number3 = [int(input()) for _ in range(3)]

print(max(number1, number2, number3),
      number1 + number2 + number3 - max(number1, number2, number3) - min(number1, number2, number3),
      min(number1, number2, number3), sep='\n')


