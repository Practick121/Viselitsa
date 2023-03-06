dlina_p = int(input())
pole = ["_"] * dlina_p
ai_points = 0
pl_points = 0
ochered = True


def random_color(elem1=' ', elem2=' '):
    color = {"B"}
    color.add("G")
    color.add("R")
    color.discard(elem1)
    color.discard(elem2)
    return color.pop()


def vivod(color, index):
    global ai_points
    global pl_points
    global ochered
    global pole
    if ochered:
        print("AI step", index, color)
    else:
        print("Your step", index, color)
    pole[index] = color
    pole_str = ''.join(pole)
    print(" ".join(pole))
    if color * 3 in pole_str:
        if ochered:
            ai_points += 1
        else:
            pl_points += 1
        i = pole_str.find(color * 3)
        pole = [pole[j] if j != i and j != i + 1 and j != i + 2 else "_" for j in range(len(pole))]
        print(' '.join(pole))
    ochered = True * (not ochered) + False * (ochered)


def two_in_row(color):
    xod = ''.join(pole).find(color * 2)
    if xod + 2 < dlina_p and pole[xod + 2] == "_":
        vivod(color, xod + 2)
    elif xod - 1 >= 0 and pole[xod - 1] == "_":
        vivod(color, xod - 1)


def two_dashes(index):
    if index > 0 and index + 2 < dlina_p:
        if pole[index - 1] == pole[index + 2]:
            vivod(random_color(pole[index + 2]), index)
        elif pole[index - 1] != pole[index + 2]:
            vivod(random_color(pole[index - 1], pole[index + 2]), index)

    elif index == 0:
        vivod(random_color(pole[index + 2]), index)
    elif index + 2 == dlina_p:
        vivod(random_color(pole[index - 1]), index)


def three_dashes(index):
    if index > 0 and index + 3 < dlina_p:
        if index - 1 != index + 3:
            vivod(pole[index - 1], index + 2)
        else:
            vivod(random_color(pole[index - 1]), index)
    elif index == 0:
        if pole[index + 3] != '_':
            vivod(pole[index + 3], index)
        else:
            vivod(random_color(), index + 1)
    elif index + 3 == dlina_p:
        vivod(pole[index - 1], index + 2)


while '_' in pole:
    if ochered:

        str_pole = ''.join(pole)
        proh_i = 0
        for i in range(1, len(pole)):
            if pole[i] == pole[proh_i] and pole[i] != "_":
                two_in_row(pole[i])

            elif i < len(pole) - 1 and pole[proh_i] != "_" and pole[proh_i] == pole[i + 1] and pole[i] == '_':
                vivod(pole[proh_i], i)
            if not ochered:
                break

            proh_i += 1
        else:
            if str_pole.count("___") > 0:
                three_dashes(str_pole.find("___"))
            elif str_pole.count("__") > 0:
                two_dashes(str_pole.find("__"))
        if ochered:
            pole1 = [i for i in range(len(pole)) if pole[i] == "_"]
            vivod(random_color(), list(set(pole1)).pop())
    else:
        plz = input().upper()
        while len(plz.split()) != 2 or not plz.split()[0].isdigit() or pole[int(plz[:-2])] != "_" or plz[-1] not in "RGB":
            if len(plz.split()) != 2 or not plz.split()[0].isdigit():
                plz = input("non direct input! ").upper()
            elif pole[int(plz[:-2])] != "_":
                plz = input("This place is taken.").upper()
            else:
                plz = input("there is no such letter!").upper()

        vivod(plz[-1:], int(plz[:-2]))
else:
    text = "AI win!" * (ai_points > pl_points) + "You win!" * (ai_points < pl_points) + "We have a tie." * (
            ai_points == pl_points)
    print(text)
    if text != "We have a tie.":
        print(ai_points, ":", pl_points)


