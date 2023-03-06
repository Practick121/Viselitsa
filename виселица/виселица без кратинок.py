import  pygame
import sys
WIDTH = 800
HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
FPS = 50
objects = []
text_sprites = []
started = False

def start():
    global started
    print("Start!")
    started = True
def vvod(vopros, vari = [], *args):
    otvet = input(vopros + ' ' + "(" + '/'.join(vari) + ') ')
    while otvet not in vari:
        otvet = input("(" + '/'.join(vari) + ')' + "? ")
    return otvet
def mainmenu():
    global buttonstart
    global title
    while not started:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
        Button.events()
        for elem in text_sprites:
            elem.output()
            pygame.display.update(elem.rect)
    objects.remove(buttonstart)
    del buttonstart
    text_sprites.remove(title)
    del title
def gameplay():
    global started
    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
        Button.events()
        for elem in text_sprites:
            elem.output()
            pygame.display.update(elem.rect)
        pygame.display.flip()

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
        self.text = font.render(text_s, True, (20, 20, 20))
        self.fillcolors = {"normal": self.color, "hover": (102, 102, 102), "pressed": (51, 51, 51)}
        self.press = False
        objects.append(self)
    def process(self):
        pos = pygame.mouse.get_pos()
        touch = pygame.mouse.get_pressed()[0]
        self.surface.fill(self.fillcolors["normal"])
        if self.rect.collidepoint(pos):
            self.surface.fill(self.fillcolors["hover"])
            if touch:
                self.surface.fill(self.fillcolors["pressed"])
                self.press = True
            elif self.press:
                self.func()
                self.press = False
        else:
            self.press = False
        self.surface.blit(self.text, (self.rect.width / 2 - self.text.get_rect().width / 2,\
                                      self.rect.height / 2 - self.text.get_rect().height / 2))
        window.blit(self.surface, self.rect)
    @classmethod
    def events(cls):
        for elem in objects:
            elem.process()
            pygame.display.update(elem.rect)



class texts(pygame.sprite.Sprite):

    def __init__(self, x, y, text, color, font):
        pygame.sprite.Sprite.__init__(self)
        self.font = font
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - self.rect.height / 2)
        text_sprites.append(self)
    def output(self):
        window.blit(self.image, self.rect)
        pygame.display.update(self.rect)


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BLUE)
pygame.display.set_caption("виселица")
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

title = texts(WIDTH / 2, HEIGHT / 4, "ВИСЕЛИЦА 2Д", PURPLE, pygame.font.Font(None, 100))
pygame.display.flip()
buttonstart = Button(100, 40, WIDTH / 2 - 50, HEIGHT / 2 - 10, GREEN, "СТАРТ!", start)



mainmenu()
gameplay()
