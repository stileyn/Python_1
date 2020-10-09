primary_color1 = input()
primary_color2 = input()

if (primary_color1 == "красный" and primary_color2 == "синий") or \
        (primary_color1 == "синий" and primary_color2 == "красный"):
    print("фиолетовый")

elif primary_color1 == "красный" and primary_color2 == "красный":
    print("красный")

elif (primary_color1 == "синий" and primary_color2 == "желтый") or \
        (primary_color1 == "желтый" and primary_color2 == "синий"):
    print("зеленый")

elif primary_color1 == "синий" and primary_color2 == "синий":
    print("синий")

elif (primary_color1 == "желтый" and primary_color2 == "красный") or \
        (primary_color1 == "красный" and primary_color2 == "желтый"):
    print("оранжевый")

elif primary_color1 == "желтый" and primary_color2 == "желтый":
    print("желтый")

else:
    print("ошибка цвета")
