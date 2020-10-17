# Дано натуральное число. Напишите программу, которая вычисляет:
#
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

def all_include(n):
    number_of_digits = 0
    last_number, last_count = n % 10, 0
    amount_of_even_numbers = 0
    summa_numbers = 0
    product_of_numbers = 1
    number_0_or_5 = 0

    while n > 0:
        if n % 10 == 3:
            number_of_digits += 1
        if last_number == n % 10:
            last_count += 1
        if n % 10 % 2 == 0:
            amount_of_even_numbers += 1
        if n % 10 > 5:
            summa_numbers += n % 10
        if n % 10 > 7:
            product_of_numbers *= n % 10
        if n % 10 == 0 or n % 10 == 5:
            number_0_or_5 += 1
        n //= 10

    print(number_of_digits)
    print(last_count)
    print(amount_of_even_numbers)
    print(summa_numbers)
    print(product_of_numbers)
    print(number_0_or_5)


all_include(int(input()))
