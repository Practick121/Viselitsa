# ИМПОРТ ВСЕХ МОДУЛЕЙ
import  pygame
import sys
import random
import os



# ОПРЕДЕЛЕНИЕ КОНСТАНТ
WIDTH = 1200
HEIGHT = 800
RED =(255, 0 ,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
X_FIRST = 100
Y_FIRST = 400
FPS = 30
SIMV = "_" # то как будет показываться неугаданный символ

 # ОПРЕДЕЛЕНИЕ ЗНАЧИМЫХ ПЕРЕМЕННЫХ
def opred():
    global objects
    global text_sprites
    global started
    global win
    global gameover
    global let
    global number_of_costum
    objects = []
    text_sprites = []
    started = False
    win = False
    gameover = False
    let = ''
    number_of_costum = 0


# ОПРЕДЕЛЕНИЕ ГЛОБАЛЬНЫХ ФУНКЦИЙ
def start(text_but):
    global started
    print("Start!")
    started = True

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def final(final):
    global final_text
    global restart
    global net
    final_text = texts(WIDTH / 2, HEIGHT / 2, "Хотите начать сначала?", (102, 102, 102), bigfont)
    final_text2 = texts(WIDTH / 2, HEIGHT / 2 - 50, "Правильное слово - " + secret, YELLOW, bigfont)
    restart = Button(200, 50, WIDTH / 2 - 100, HEIGHT * 0.65, (102, 102, 102), "СНАЧАЛА", main)
    net = Button(200, 50, WIDTH / 2 - 100, HEIGHT * 0.75, (102, 102, 102), "НЕТ", sys.exit)
    if final == 1:
        print("о еда")
        oboi = pygame.transform.scale(pygame.image.load(resource_path(r'images\победа.jpg')), (WIDTH, HEIGHT))
    else:
        oboi = pygame.transform.scale(pygame.image.load(resource_path(r'images\поражение.jpg')), (WIDTH, HEIGHT))
        print('еее !')
    while 1:
        window.blit(oboi, (0, 0))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
        final_text.output()
        final_text2.output()
        restart.process('')
        net.process('')
        pygame.display.flip()
def letter_press(let):
    global set_povt
    global win
    global number_of_costum
    global gameover
    global pole
    global sprite_pole
    print(let)
    if let in secret and let not in set_povt:
        print("Правильно!")
        for j in poisk(let):
            print("Замена")
            pole[j] = let
        if SIMV not in pole:
            print("ПОБЕДА")
            win = True

    elif let in set_povt:
        print("Уже было!")
        return
    else:
        print("Неправильно!")
        number_of_costum += 1
        if number_of_costum > 9:
            gameover = True
    set_povt.add(let)
    text_sprites.remove(sprite_pole)
    sprite_pole = texts(WIDTH * 0.65, 200, '  '.join(pole), BLACK, bigfont)
    print(pole)
    print(sprite_pole.text)
    #sprite_pole.font.render(sprite_pole.text, True, sprite_pole.color)

def poisk(b):
    otvet = []
    for i in range(len(secret)):
        if secret[i] == b:
            otvet.append(i)
    return otvet



def mainmenu(text_but=''):
    global back_ground_menu_rect
    global back_ground_menu
    title = texts(WIDTH / 2, HEIGHT / 4, "ВИСЕЛИЦА 2Д", PURPLE, pygame.font.Font(None, 100))
    buttonstart = Button(100, 40, WIDTH / 2 - 50, HEIGHT / 2 - 10, GREEN, "СТАРТ!", start)
    window.blit(back_ground_menu, back_ground_menu_rect)
    pygame.display.flip()
    while not started:
        window.blit(back_ground_menu, (0, 0))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if not buttonstart.rect.collidepoint(mouse_pos) and back_ground_menu_rect.collidepoint(mouse_pos):
                        back_ground_menu = pygame.transform.flip(back_ground_menu, True, False)
                        pygame.display.update(back_ground_menu_rect)
        for elem in objects:
            elem.process("")
            pygame.display.update(elem.rect)
        for elem in text_sprites:
            elem.output()
            pygame.display.update(elem.rect)
        pygame.display.flip()

    objects.remove(buttonstart)
    del buttonstart
    text_sprites.remove(title)
    del title



def gameplay():
    global started
    global let
    global objects
    global sprite_pole
    global dubl_pole
    sprite_pole = texts(WIDTH * 0.65, 200, '  '.join(pole), BLACK, bigfont)
    print(len(text_sprites))
    q1 = Button(50, 50, X_FIRST, Y_FIRST, RED, "Й", letter_press)
    w1 = Button(50, 50, X_FIRST + 75, Y_FIRST, RED, "Ц", letter_press)
    e1 = Button(50, 50, X_FIRST + 150, Y_FIRST, RED, "У", letter_press)
    r1 = Button(50, 50, X_FIRST + 225, Y_FIRST, RED, "К", letter_press)
    t1 = Button(50, 50, X_FIRST + 300, Y_FIRST, RED, "Е", letter_press)
    y1 = Button(50, 50, X_FIRST + 375, Y_FIRST, RED, "Н", letter_press)
    u1 = Button(50, 50, X_FIRST + 450, Y_FIRST, RED, "Г", letter_press)
    i1 = Button(50, 50, X_FIRST + 525, Y_FIRST, RED, "Ш", letter_press)
    o1 = Button(50, 50, X_FIRST + 600, Y_FIRST, RED, "Щ", letter_press)
    p1 = Button(50, 50, X_FIRST + 675, Y_FIRST, RED, "З", letter_press)
    p2 = Button(50, 50, X_FIRST + 750, Y_FIRST, RED, "Х", letter_press)
    p3 = Button(50, 50, X_FIRST + 825, Y_FIRST, RED, "Ъ", letter_press)
    a1 = Button(50, 50, X_FIRST + 25, Y_FIRST + 100, RED, "Ф", letter_press)
    s1 = Button(50, 50, X_FIRST + 100, Y_FIRST + 100, RED, "Ы", letter_press)
    d1 = Button(50, 50, X_FIRST + 175, Y_FIRST + 100, RED, "В", letter_press)
    f1 = Button(50, 50, X_FIRST + 250, Y_FIRST + 100, RED, "А", letter_press)
    g1 = Button(50, 50, X_FIRST + 325, Y_FIRST + 100, RED, "П", letter_press)
    h1 = Button(50, 50, X_FIRST + 400, Y_FIRST + 100, RED, "Р", letter_press)
    j1 = Button(50, 50, X_FIRST + 475, Y_FIRST + 100, RED, "О", letter_press)
    k1 = Button(50, 50, X_FIRST + 550, Y_FIRST + 100, RED, "Л", letter_press)
    l1 = Button(50, 50, X_FIRST + 625, Y_FIRST + 100, RED, "Д", letter_press)
    l2 = Button(50, 50, X_FIRST + 700, Y_FIRST + 100, RED, "Ж", letter_press)
    l3 = Button(50, 50, X_FIRST + 775, Y_FIRST + 100, RED, "Э", letter_press)
    z1 = Button(50, 50, X_FIRST + 50, Y_FIRST + 200, RED, "Я", letter_press)
    x1 = Button(50, 50, X_FIRST + 125, Y_FIRST + 200, RED, "Ч", letter_press)
    c1 = Button(50, 50, X_FIRST + 200, Y_FIRST + 200, RED, "С", letter_press)
    v1 = Button(50, 50, X_FIRST + 275, Y_FIRST + 200, RED, "М", letter_press)
    b1 = Button(50, 50, X_FIRST + 350, Y_FIRST + 200, RED, "И", letter_press)
    n1 = Button(50, 50, X_FIRST + 425, Y_FIRST + 200, RED, "Т", letter_press)
    m1 = Button(50, 50, X_FIRST + 500, Y_FIRST + 200, RED, "Ь", letter_press)
    m2 = Button(50, 50, X_FIRST + 575, Y_FIRST + 200, RED, "Б", letter_press)
    m3 = Button(50, 50, X_FIRST + 650, Y_FIRST + 200, RED, "Ю", letter_press)
    while not win and not gameover:
        window.fill((255, 222, 90))
        window.blit(dubl, main_char_rect)
        window.blit(main_char[number_of_costum], main_char_rect)
        for elem in objects:
            elem.process(elem.text_s.lower())
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        for elem in text_sprites:
            elem.output()
        pygame.display.flip()
        clock.tick(FPS)
    objects = []
    del q1, w1, e1, r1, t1, y1, u1, i1, o1, p1, p2, p3, a1, s1, d1, f1, g1, h1, j1, k1, l1, l2, l3, z1, x1, c1, v1, b1, n1, m1, m2, m3

# ОПРЕДЕЛЕНИЕ КЛАССОВ (шаблоны, по которым будут созданы спрайты)
class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color, text_s="Button", func=None):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.func = func
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_s = text_s
        self.text = font.render(self.text_s, True, (20, 20, 20))
        self.press = False
        objects.append(self)
    def process(self, text_but):
        self.fillcolors = {"normal": self.color, "hover": (102, 102, 102), "pressed": (51, 51, 51)}
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
                    self.color = GREEN
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

# ИНИЦИАЛИЗАЦИЯ
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("виселица")
font = pygame.font.Font(None, 30)
bigfont = pygame.font.Font(None, 75)
clock = pygame.time.Clock()



# СКАЧИВАНИЕ ФАЙЛОВ
spisok = open(resource_path('texts/russian_nouns.txt'), encoding='utf-8').readlines()
main_char = [pygame.Surface((500, 500), pygame.SRCALPHA),
        pygame.image.load(resource_path(r"images\виселица2.png")),
        pygame.image.load(resource_path(r"images\виселица3.png")),
        pygame.image.load(resource_path(r"images\виселица4.png")),
        pygame.image.load(resource_path(r"images\виселица5.png")),
        pygame.image.load(resource_path(r"images\виселица6.png")),
        pygame.image.load(resource_path(r"images\виселица7.png")),
        pygame.image.load(resource_path(r"images\виселица8.png")),
        pygame.image.load(resource_path(r"images\виселица9.png")),
        pygame.image.load(resource_path(r'images\виселица10.png'))]
main_char_rect = main_char[0].get_rect(topleft=(-100, -50))

dubl = pygame.image.load(resource_path(r'images\виселица11.png'))
back_ground_menu = pygame.transform.scale(pygame.image.load(resource_path(r"images\заднийфон.jpg")).convert(), (WIDTH, HEIGHT))
back_ground_menu_rect = back_ground_menu.get_rect(topleft=(0, 0))

# ИНИЦИАЛИЗАЦИЯ 2
def initil():
    global k
    global secret
    global pole
    global set_povt
    k = random.randint(1, 51302)
    secret = spisok[k][:-1] # случайно сгенерированное слово
    while len(secret) > 7 or len(secret) < 4 or "ё" in secret:
        print(secret)
        k = random.randint(1, 51302)
        secret = spisok[k][:-1]
    pole = [SIMV] * len(secret)
    set_povt = set()
    print(secret + " <=")


# ЗАПУСК
def main(text_but=''):
    opred()
    initil()
    mainmenu()
    gameplay()
    final(1 * (win))

main()