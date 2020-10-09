# На вход программе подается число n – количество собачьих лет. Напишите программу,
# которая вычисляет возраст собаки в человеческих годах.

dog_age = int(input())
human_age = 0

for i in range(1, dog_age + 1):
    if i == 1 or i == 2:
        human_age += 10.5
    else:
        human_age += 4

print(human_age)