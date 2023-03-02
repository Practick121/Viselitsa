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
def vvod(vopros, vari = [], *args):
    otvet = input(vopros + ' ' + "(" + '/'.join(vari) + ') ')
    while otvet not in vari:
        otvet = input("(" + '/'.join(vari) + ')' + "? ")
    return otvet

def start():
    print("Приветствую!")

class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color, text_s):
        super().__init__()
        self.image = pygame.Surface((width, height)).fill(color)
        self.image.blit(text_s, (self.image.get_width() / 2 - text_s.get_width(),\
                                 self.image.get_height() / 2 - text_s.get_height()))
        self.rect = self.image.get_rect(center=(x - width / 2, y - height / 2))
    def touch_m(self):
        pos = pygame.mouse.get_pos()
        if self.rect.right >= pos[0] >= self.rect.left and self.rect.top <= pos[1] <= self.rect.bottom:
            for i in pygame.event.get():
                if i.type == pygame.MOUSEBUTTONUP:
                    return True
        return False
    def output(self, screen):
        screen.blit(self.image, self.rect)
        pygame.display.update(self.rect)





class texts(pygame.sprite.Sprite):
    def __init__(self, x, y, text, color, font):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect(center=(x, y))
    def output(self, screen):
        screen.blit(self.image, self.rect)
        pygame.display.update(self.rect)


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BLUE)
pygame.display.set_caption("виселица")
font = pygame.font.Font(None, 30)

text_sprites = pygame.sprite.Group()
pygame.display.flip()
started = True
start()
buttonst_t = texts(0, 0, YELLOW, "страт", font)
buttonst = Button(50, 50, WIDTH // 2, HEIGHT // 2, BLACK, buttonst_t.image)
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    if started:
        window.fill(BLUE)
        buttonst.output(window)
        if buttonst.touch_m():
            print('х')
    text_sprites.draw(window)
    pygame.display.flip()