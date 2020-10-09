# put your python code here
age = int(input())
if age <= 13:
    print('детство')
elif 14 <= age <= 24:
    print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
elif age >= 60:
    print('старость')