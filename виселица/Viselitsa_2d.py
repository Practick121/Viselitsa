# ИМПОРТ ВСЕХ МОДУЛЕЙ
import pygame
import sys
import random
import os


# ОПРЕДЕЛЕНИЕ КОНСТАНТ
RED = (255, 0 ,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
BLUE = (50, 100, 215)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0) # основные цвета в RGB
X_FIRST, Y_FIRST = 100, 400 # координаты первой кнопки
FPS = 30 # задержка
SIMV = "_" # то как будет показываться неугаданный символ


def exit_close(but=''): # функция срабатывает при нажатии на кресстик или кнопку выход
    global user_data
    user_data.seek(0)
    user_data.write(str(level) + '\n' + str(coins) + "\n" + str(VOLUME))
    user_data.close() # данные пользователя записываются в файл
    sys.exit()


 # ОПРЕДЕЛЕНИЕ ЗНАЧИМЫХ ПЕРЕМЕННЫХ
def opred():
    global objects
    global text_sprites
    global to_game
    global win
    global gameover
    global let
    global number_of_costum
    global to_option
    global level
    global user_data
    global coins
    objects = [] # список кнопок
    text_sprites = [] # список всех надписей
    to_game = False # флаг, определяющий находится ли пользователь в геймплейной части
    to_option = False # флаг, определяющий находится ли пользователь в правилах
    win = False # флаг, показывающий выиграл ли игрок
    gameover = False # флаг, показывающий проиграл ли игрок
    let = '' # нажатая буква
    number_of_costum = 0 # костюм виселицы


# ОПРЕДЕЛЕНИЕ ГЛОБАЛЬНЫХ ФУНКЦИЙ
def start(text_but): # функция, вызывающаяся кнопкой старт
    global to_game
    to_game = True



def volume(text_but=''): # функция, вызывающаяся при нажатии кнопки VOLUME
    global volume_but
    global sprite_gr
    global VOLUME
    if volume_but.text == sprite_gr[0]: # если звук включен
        VOLUME = 0
        volume_but.text = sprite_gr[1]
    else: # если звук выключен
        VOLUME = 1
        volume_but.text = sprite_gr[0]
    pygame.mixer.music.set_volume(VOLUME)
    pygame.display.update(volume_but.rect) # обновление нужной части экрана


def resource_path(relative_path): # важная функция при работе с файлами
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def final(final): # после того, как пользователь угадал слово или проиграл
    global final_text
    global restart
    global net
    global level
    global user_data
    global coins
    pygame.time.delay(500)
    pygame.mixer.quit()
    pygame.mixer.init() # небольшая задержка и простое удаление всех воспроизводимых звуков
    pygame.mixer.music.set_volume(VOLUME)
    restart = Button(200, 50, WIDTH / 2 - 100, HEIGHT * 0.65, (102, 102, 102), "главное меню", main) #создание кнопки перезапуска
    if final == 1:
        final_text = texts(WIDTH / 2, HEIGHT * 0.3, f"Уровень {level} пройден! \n  \n  + {level * 462} сошиал кредиц", RED, bigfont)
        coins += level * 462
        oboi = pygame.transform.scale(pygame.image.load(resource_path(r'images/победа3.png')), (WIDTH * 2.5, HEIGHT))
        pygame.mixer.music.load(resource_path(r'music/победа.mp3'))
        level += 1
    else:
        oboi = pygame.transform.scale(pygame.image.load(resource_path(r'images/поражение3.png')), (WIDTH, HEIGHT + 400))
        pygame.mixer.music.load(resource_path(r'music/поражение2.mp3'))
        final_text = texts(WIDTH / 2, HEIGHT * 0.3, "Правильное слово - " + secret, RED, bigfont)
    pygame.mixer.music.play()
    while 1:
        if final == 1:
            window.blit(oboi, (-WIDTH + 100, 0))
        else:
            window.blit(oboi, (0, -200))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit_close()
        final_text.output()
        restart.process('')
        pygame.display.flip()


def back_to(text_but=''):
    global to_option
    to_option = False


def go_option(text_but=''):
    global to_option
    to_option = True


def option():
    global bac
    global to_option
    global volume_but
    volume_but = Button(50, 50, 50, HEIGHT * 0.8, (0, 0, 0, 0), "@звук", volume)
    bac = Button(200, 50, 100, HEIGHT * 0.9, RED, "назад", back_to)
    info = "ПРАВИЛА"
    rulestext = r"""Помоги себе набрать социального статуса!
    
    Решай головоломки и получай кредиты! 
    
    Каждый раз уровень будет повышаться.
    
    На каждый уровень дается 10 попыток."""
    tit = texts(WIDTH / 2, HEIGHT * 0.2, info, (51, 51, 51), bigfont)
    rules = texts(WIDTH / 2, HEIGHT * 0.65, rulestext, (120, 120, 120), pygame.font.Font(None, 50))
    window.blit(back_ground_option, back_ground_rect)
    pygame.display.flip()
    while to_option:
        window.blit(back_ground_option, (0, 0))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit_close()
        for elem in objects:
            elem.process('')
        for ele in text_sprites:
            ele.output()

        pygame.display.flip()
        clock.tick(FPS)
    objects.remove(bac)
    del bac
    objects.remove(volume_but)
    del volume_but
    text_sprites.remove(rules)
    del rules
    text_sprites.remove(tit)
    del tit
    mainmenu('')


def letter_press(let):
    global set_povt
    global win
    global number_of_costum
    global gameover
    global pole
    global sprite_pole
    if let in secret and let not in set_povt:
        for j in poisk(let):
            pole[j] = let
        if SIMV not in pole:
            win = True
        else:
            sound2 = pygame.mixer.Sound(resource_path(r'music/угадал_букву.mp3'))
            sound2.set_volume(VOLUME)
            sound2.play()

    elif let in set_povt:
        return
    else:
        sound1 = pygame.mixer.Sound(resource_path(r'music/буква_неугадана.mp3'))
        sound1.set_volume(VOLUME)
        sound1.play()
        number_of_costum += 1
        if number_of_costum > 9:
            gameover = True
    set_povt.add(let)
    text_sprites.remove(sprite_pole)
    sprite_pole = texts(WIDTH * 0.65, 200, '  '.join(pole), BLACK, bigfont)


def poisk(b):
    otvet = []
    for i in range(len(secret)):
        if secret[i] == b:
            otvet.append(i)
    return otvet


def mainmenu(text_but=''):
    global back_ground_rect
    global back_ground_menu
    global volume_but
    global options
    global buttonstart
    global title
    global exitt
    pygame.mixer.music.load(music_of_main_menu)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(VOLUME)
    title = texts(WIDTH / 2, HEIGHT / 4, "ВИСЕЛИЦА 2Д", PURPLE, pygame.font.Font(None, 100))
    buttonstart = Button(200, 50, WIDTH / 2 - 100, HEIGHT * 0.5, WHITE, "НАЧАТЬ", start)
    options = Button(200, 50, WIDTH / 2 - 100, HEIGHT * 0.6, BLUE, "ПРАВИЛА", go_option)
    exitt = Button(200, 50, WIDTH / 2 - 100, HEIGHT * 0.7, RED, "ВЫХОД", exit_close)
    volume_but =  Button(50, 50, 50, HEIGHT * 0.8, (0,0,0,0), "@звук", volume)
    credit = texts(WIDTH * 0.85, 50, f"{coins} сошиал кредиц", RED, pygame.font.Font(resource_path(r'fonts/arial.ttf'), 30))
    yrov = texts(WIDTH / 2, HEIGHT * 0.49, f"{level} уровень", BLACK, font)
    window.blit(back_ground_menu, back_ground_rect)
    pygame.display.flip()
    while not to_game and not to_option:
        window.blit(back_ground_menu, (0, 0))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit_close()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 or i.button == 3:
                    mouse_pos = pygame.mouse.get_pos()
                    touch_obj = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1).collidelist(objects)
                    if touch_obj == -1 and back_ground_rect.collidepoint(mouse_pos):
                        if i.button == 1:
                            back_ground_menu = pygame.transform.flip(back_ground_menu, True, False)
                        else:
                            back_ground_menu = pygame.transform.flip(back_ground_menu, False, True)
                        pygame.display.update(back_ground_rect)
        for elem in objects:
            elem.process("")
            pygame.display.update(elem.rect)
        for elem in text_sprites:
            elem.output()
            pygame.display.update(elem.rect)
        pygame.display.flip()

    objects.remove(buttonstart)
    del buttonstart
    objects.remove(exitt)
    del exitt
    objects.remove(options)
    del options
    text_sprites.remove(title)
    del title
    objects.remove(volume_but)
    del volume_but
    text_sprites.remove(yrov)
    del yrov
    if to_option:
        option()



def gameplay():
    global to_game
    global let
    global objects
    global sprite_pole
    global dubl_pole
    global volume_but
    volume_but = Button(50, 50, 50, HEIGHT * 0.8, (0, 0, 0, 0), "@звук", volume)
    sprite_pole = texts(WIDTH * 0.65, 200, '  '.join(pole), BLACK, bigfont)
    yrov = texts(WIDTH * 0.5, HEIGHT * 0.1, f"{level} уровень", BLACK, bigfont)
    q1 = Button(SIZE, SIZE, X_FIRST, Y_FIRST, WHITE, "Й", letter_press)
    w1 = Button(SIZE, SIZE, X_FIRST + 1 * INTERV, Y_FIRST, WHITE, "Ц", letter_press)
    e1 = Button(SIZE, SIZE, X_FIRST + 2 * INTERV, Y_FIRST, WHITE, "У", letter_press)
    r1 = Button(SIZE, SIZE, X_FIRST + 3 * INTERV, Y_FIRST, WHITE, "К", letter_press)
    t1 = Button(SIZE, SIZE, X_FIRST + 4 * INTERV, Y_FIRST, WHITE, "Е", letter_press)
    y1 = Button(SIZE, SIZE, X_FIRST + 5 * INTERV, Y_FIRST, WHITE, "Н", letter_press)
    u1 = Button(SIZE, SIZE, X_FIRST + 6 * INTERV, Y_FIRST, WHITE, "Г", letter_press)
    i1 = Button(SIZE, SIZE, X_FIRST + 7 * INTERV, Y_FIRST, WHITE, "Ш", letter_press)
    o1 = Button(SIZE, SIZE, X_FIRST + 8 * INTERV, Y_FIRST, WHITE, "Щ", letter_press)
    p1 = Button(SIZE, SIZE, X_FIRST + 9 * INTERV, Y_FIRST, WHITE, "З", letter_press)
    p2 = Button(SIZE, SIZE, X_FIRST + 10 * INTERV, Y_FIRST, WHITE, "Х", letter_press)
    p3 = Button(SIZE, SIZE, X_FIRST + 11 * INTERV, Y_FIRST, WHITE, "Ъ", letter_press)
    a1 = Button(SIZE, SIZE, X_FIRST + 25 + 0 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "Ф", letter_press)
    s1 = Button(SIZE, SIZE, X_FIRST + 25 + 1 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "Ы", letter_press)
    d1 = Button(SIZE, SIZE, X_FIRST + 25 + 2 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "В", letter_press)
    f1 = Button(SIZE, SIZE, X_FIRST + 25 + 3 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "А", letter_press)
    g1 = Button(SIZE, SIZE, X_FIRST + 25 + 4 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "П", letter_press)
    h1 = Button(SIZE, SIZE, X_FIRST + 25 + 5 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "Р", letter_press)
    j1 = Button(SIZE, SIZE, X_FIRST + 25 + 6 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "О", letter_press)
    k1 = Button(SIZE, SIZE, X_FIRST + 25 + 7 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "Л", letter_press)
    l1 = Button(SIZE, SIZE, X_FIRST + 25 + 8 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "Д", letter_press)
    l2 = Button(SIZE, SIZE, X_FIRST + 25 + 9 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "Ж", letter_press)
    l3 = Button(SIZE, SIZE, X_FIRST + 25 + 10 * INTERV, Y_FIRST + HEIGHT / 8, WHITE, "Э", letter_press)
    z1 = Button(SIZE, SIZE, X_FIRST + 50 + 1 * INTERV, Y_FIRST + 2 * HEIGHT / 8, WHITE, "Я", letter_press)
    x1 = Button(SIZE, SIZE, X_FIRST + 50 + 2 * INTERV, Y_FIRST + 2 * HEIGHT / 8, WHITE, "Ч", letter_press)
    c1 = Button(SIZE, SIZE, X_FIRST + 50 + 3 * INTERV, Y_FIRST + 2 * HEIGHT / 8, WHITE, "С", letter_press)
    v1 = Button(SIZE, SIZE, X_FIRST + 50 + 4 * INTERV, Y_FIRST + 2 * HEIGHT / 8, WHITE, "М", letter_press)
    b1 = Button(SIZE, SIZE, X_FIRST + 50 + 5 * INTERV, Y_FIRST + 2 * HEIGHT / 8, WHITE, "И", letter_press)
    n1 = Button(SIZE, SIZE, X_FIRST + 50 + 6 * INTERV, Y_FIRST + 2 * HEIGHT / 8, WHITE, "Т", letter_press)
    m1 = Button(SIZE, SIZE, X_FIRST + 50 + 7 * INTERV, Y_FIRST + 2 * HEIGHT / 8, WHITE, "Ь", letter_press)
    m2 = Button(SIZE, SIZE, X_FIRST + 50 + 8 * INTERV, Y_FIRST + 2 * HEIGHT / 8, WHITE, "Б", letter_press)
    m3 = Button(SIZE, SIZE, X_FIRST + 50 + 9 * INTERV, Y_FIRST + 2 * HEIGHT / 8, WHITE, "Ю", letter_press)
    while not win and not gameover:
        window.fill((255, 222, 90))
        window.blit(dubl, main_char_rect)
        window.blit(main_char[number_of_costum], main_char_rect)
        for elem in objects:
            elem.process(elem.text_s.lower())
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit_close()
        for elem in text_sprites:
            elem.output()
        pygame.display.flip()
        clock.tick(FPS + 10)
    objects = []
    del q1, w1, e1, r1, t1, y1, u1, i1, o1, p1, p2, p3, a1, s1, d1, f1, g1, h1, j1, k1, l1, l2, l3, z1, x1, c1, v1, b1, n1, m1, m2, m3
    text_sprites.remove(yrov)
    del yrov


# ОПРЕДЕЛЕНИЕ КЛАССОВ (шаблоны, по которым будут созданы спрайты)
class Button(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y, color, text_s="Button", func=None):
        global sprite_gr
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.func = func
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_s = text_s
        if self.text_s[0] == '@':
            if text_s == "@звук":
                sprite_gr = [pygame.transform.scale(i, (self.width, self.height)) for i in sprite_gr]
                self.text = sprite_gr[1 - VOLUME]
                self.fillcolors = {"normal": self.color, "hover": self.color, "pressed": self.color}
        else:
            self.text = font.render(self.text_s, True, (20, 20, 20))
            self.fillcolors = {"normal": self.color, "hover": (102, 102, 102), "pressed": (51, 51, 51)}
        self.press = False
        objects.append(self)
    def process(self, text_but):
        self.fillcolors["normal"] = self.color
        pos = pygame.mouse.get_pos()
        touch = pygame.mouse.get_pressed()[0]
        self.surface.fill(self.fillcolors["normal"])
        if self.rect.collidepoint(pos):
            self.surface.fill(self.fillcolors["hover"])
            if touch:
                self.surface.fill(self.fillcolors["pressed"])
                self.press = True
            elif self.press:
                if len(self.text_s) == 1:
                    if self.text_s.lower() in secret:
                        self.color = GREEN
                        self.fillcolors["hover"] = GREEN
                    else:
                        self.color = RED
                        self.fillcolors["hover"] = RED
                self.func(text_but)
                self.press = False
        else:
            self.press = False
        self.surface.blit(self.text, (self.rect.width / 2 - self.text.get_rect().width / 2,\
                                      self.rect.height / 2 - self.text.get_rect().height / 2))
        window.blit(self.surface, self.rect)



class texts(pygame.sprite.Sprite):

    def __init__(self, x, y, text, color, font):
        pygame.sprite.Sprite.__init__(self)
        self.font = font
        self.text = text
        self.color = color
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - self.rect.height / 2)
        text_sprites.append(self)

    def output(self):
        window.blit(self.image, self.rect)
        pygame.display.update(self.rect)




# ИНИЦИАЛИЗАЦИЯ 2
def initil():
    global k
    global secret
    global pole
    global set_povt
    if level >= 4:
        k = random.randint(0, 51302)
        secret = spisok[k][:-1] # случайно сгенерированное слово
        while len(secret) > 7 or len(secret) < 4 or "ё" in secret:
            k = random.randint(1, 51302)
            secret = spisok[k][:-1]
    elif level == 1:
        k = random.randint(0, 24)
        secret = easy[k][:-1]
    elif level == 2:
        k = random.randint(0, 17)
        secret = normal[k][:-1]
    elif level == 3:
        k = random.randint(0, 14)
        secret = hard[k][:-1]
    pole = [SIMV] * len(secret)
    set_povt = set()
    #print(secret + " <=")


# ЗАПУСК
def main(text_but=''):

    opred()
    initil()
    mainmenu()
    gameplay()
    final(1 * (win))


if __name__ == '__main__':
    # ИНИЦИАЛИЗАЦИЯ
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h - 50
    INTERV = (WIDTH - X_FIRST) / 14
    SIZE = INTERV / 3 * 2
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ВИСЕЛИЦА.ультра")
    font = pygame.font.Font(resource_path(r"fonts/arial.ttf"), 30)
    bigfont = pygame.font.Font(None, 75)
    clock = pygame.time.Clock()
    try:
        user_data = open("user_Viselitsa", mode="r+")
        user_data.seek(0)
        level = int(user_data.readline())
        coins = int(user_data.readline())
        VOLUME = int(user_data.readline())
    except Exception:
        print("Не получилось")
        user_data = open("user_Viselitsa", mode="w+")
        user_data.write("1" + "\n" + "0" + "\n" + "1")
        user_data.seek(0)
        level = 1
        coins = 0
        VOLUME = 1

    # СКАЧИВАНИЕ ФАЙЛОВ
    spisok = open(resource_path('texts/russian_nouns.txt'), encoding='utf-8').readlines()
    easy = open(resource_path(r"texts/easy"), encoding='utf-8').readlines()
    normal = open(resource_path(r"texts/normal"), encoding='utf-8').readlines()
    hard = open(resource_path(r'texts/hardcore'), encoding='utf-8').readlines()
    main_char = [pygame.Surface((500, 500), pygame.SRCALPHA),
                 pygame.image.load(resource_path(r"images/виселица2.png")),
                 pygame.image.load(resource_path(r"images/виселица3.png")),
                 pygame.image.load(resource_path(r"images/виселица4.png")),
                 pygame.image.load(resource_path(r"images/виселица5.png")),
                 pygame.image.load(resource_path(r"images/виселица6.png")),
                 pygame.image.load(resource_path(r"images/виселица7.png")),
                 pygame.image.load(resource_path(r"images/виселица8.png")),
                 pygame.image.load(resource_path(r"images/виселица9.png")),
                 pygame.image.load(resource_path(r'images/виселица10.png'))]
    main_char_rect = main_char[0].get_rect(topleft=(-100, -50))
    sprite_gr = [pygame.image.load(resource_path(r'images/громкость.png')),
                 pygame.image.load(resource_path(r"images/громкость_зачеркнт.png"))]
    dubl = pygame.image.load(resource_path(r'images/виселица11.png'))
    back_ground_menu = pygame.transform.scale(pygame.image.load(resource_path(r"images/главное_меню.png")).convert(),
                                              (WIDTH, HEIGHT))
    back_ground_option = pygame.transform.scale(pygame.image.load(resource_path(r'images/правли2.png')).convert(), \
                                                (WIDTH, HEIGHT))
    back_ground_rect = back_ground_menu.get_rect(topleft=(0, 0))
    music_of_main_menu = resource_path(r'music/главное_меню.mp3')


    main()
