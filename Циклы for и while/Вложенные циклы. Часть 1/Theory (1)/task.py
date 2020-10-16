#  28n+30k+31m=365.

def korni():
    for n in range(1, 14):
        for k in range(1, 13):
            for m in range(1, 12):
                if 28 * n + 30 * k + 31 * m == 365:
                    print('n =', n, 'k =', k, 'm =', m)


#  Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если
#  плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля и надо купить 100 голов скота?

def korni_1():
    for q in range(1, 11):
        for w in range(1, 21):
            for r in range(1, 201):
                if q + w + r == 100:
                    if 10 * q + 5 * w + 0.5 * r == 100:
                        print(q, w, r)


# Гипотеза Эйлера о сумме степеней

def korni_2():
    num_5 = {num: num ** 5 for num in range(1, 160)}
    abc_5 = {a_v + b_v + c_v: (a, b, c) for a, a_v in num_5.items() for b, b_v in num_5.items() for c, c_v in
             num_5.items()}
    de_5 = {e_v - d_v: (d, e) for e, e_v in num_5.items() for d, d_v in num_5.items()}
    equals = abc_5.keys() & de_5.keys()
    for equal in equals:
        print("a=%s, b=%s, c=%s," % abc_5[equal], "d=%s, e=%s" % de_5[equal])


korni()
korni_1()
korni_2()
