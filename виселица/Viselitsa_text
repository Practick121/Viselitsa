import random
print("Вначале игра поинтересуется, сколько бы хотелось макс букв в слове? советую писать целые числа")
print("Затем программа загадывает случайное слово из 51302 слов, поэтому некоторые из слов могут быть совсем не известны.")
print("Игра будет длиться до тех пор, пока ты не отгадаешь слово или же пока ты не психанешь и выключишь комп")
print("После мучительного отгадывания, программа подскажет сколько попыток ты потратил(а) и вежливо намекнёт отложить гаджет и заняться делом")
print("Есть одна команда - !help, не знаю зачем она нужна, но она выведет предыдущие три строки, когда ты ее напишешь вместо буквы")

def initil():
    global i
    global n
    global k
    global spisok
    global secret
    global pole
    global povt
    n = 1
    while n not in ['5', '6', '7', '8', '9', '0']:
        n = input("Введи ограничения на количество букв в слове(от 5) =>")
        if n.replace(".", "1").isdigit() and int(float(n)) != float(n):
            print("какой плохой")
            print("советую слушать советы")
    n = int(n)
    k = random.randint(0, 51302)
    spisok = open('texts/russian_nouns.txt', encoding='utf-8').readlines()
    secret = spisok[k][:-1] # случайно сгенерированное слово
    while len(secret) > n or len(secret) < 4:
        k = random.randint(1, 51302)
        secret = spisok[k][:-1] # случайно сгенерированное слово
    pole = ["_"] * len(secret)
    povt = set() # список повторяющихся букв
    i = 0
    print(''.join(pole))
def poisk(b, slovo):
    otvet = []
    for i in range(len(slovo)):
        if slovo[i] == b:
            otvet.append(i)
    return otvet
def main():
    global i
    global otvet
    global povt
    while "_" in pole:
        otvet = input("Введи букву или слово => ")
        if otvet == "!help":
            print("Вначале введи желаемое максимальное количество букв в загадываевом слове")
            print("Затем программа загадывает случайное слово из 51302 слов, поэтому некоторые из слов могут быть совсем не известны.")
            print("Игра будет длиться до тех пор, пока ты не отгадаешь слово или же пока ты не психанешь и выключишь комп")
            print("""После мучительного отгадывания, программа подскажет сколько попыток ты потратил(а)
и вежливо намекнёт отложить гаджет и заняться делом(а может уже сейчас?)""")
            continue
        if len(otvet) > 1 and otvet == secret:
            break
        elif len(otvet) > 1:
            print("Неверно!")
            i += 1
            continue
        if ord(otvet) < 1040 or ord(otvet) > 1103:
            print("Походу ты ввел что-то не то.", end=' ')
            continue

        otvet = otvet.lower()
        if otvet in secret and otvet not in povt:
            print("Правильно!")
            i += 1
            for j in poisk(otvet, secret):
                pole[j] = otvet
        elif otvet in povt:
            print("Уже было!")
        else:
            print("Неправильно!")
            i += 1
        print(''.join(pole))
        povt.add(otvet)

    print(f"Победа! ты угадала слово за {i} попыток (считая попытки, когда угадано)")
    print("Желаешь выйти или остаться?")
    otvet = input()
    while otvet not in ["уйти", "остаться"]:
        otvet = input("уйти/остаться =>")
    if otvet == "уйти":
        print("Не забудь посетить мой гитхаб")
        exit()
    initil()
    print("""РЕКЛАМА
    Хватит  играть в этот отстой! На на моём гитхаб есть 2д версия этой игры, которая во всем лучше этой!""")
    main()

initil()
main()
