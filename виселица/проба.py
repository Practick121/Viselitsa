import random
n = input("Введите желаемое количество букв в слове, от 3 ('0', если до 6) =>")
while n not in ['4', '5', '6', '7', '8', '9', '0']:
    n = input("Введите желаемое количество букв в слове, от 3 ('0', если до 6) =>")
n = int(n)
k = random.randint(1, 51302)
spisok = open('russian_nouns.txt', encoding='utf-8').readlines()
secret = spisok[k][:-1] # случайно сгенерированное слово
while len(secret) != n and n != 0:
    k = random.randint(1, 51302)
    secret = spisok[k][:-1] # случайно сгенерированное слово
pole = ["*"] * len(secret)

i = 0
def poisk(b, slovo):
    otvet = []
    for i in range(len(slovo)):
        if slovo[i] == b:
            otvet.append(i)
    return otvet
while i < 6:

    print(''.join(pole))
    otvet = input("Введи букву => ")
    while len(otvet) != 1:
        otvet = input("1 буква! еще раз => ")
    while ord(otvet) < 1040 or ord(otvet) > 1103:
        otvet = input("Походу ты ввел что-то не то, еще раз => ")
    otvet = otvet.lower()
    if otvet in secret:
        print("Правильно!")
        for j in poisk(otvet, secret):
            pole[j] = otvet
        if "*" not in pole:
            break
    else:
        print("Неправильно!")
        print(f"Осталось {5 - i} попыток!")
        i += 1


else:
    print("К сожелению, гейм овер((")
    exit()
print("ПОБЕДА")