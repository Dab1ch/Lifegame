from numba import njit
import pygame

pygame.init()

c = int(input())
game = 1
n = 800000
width = 1
clock = pygame.time.Clock()

def check(c, lines):
    for i in range(c):
        for k in range(c):
            for b in range(i-1, i+2):
                for a in range(k-1, k+2):
                    if b == i and a == k:
                        pass
                    elif lines[int(b%c)][int(a%c)].value == 1:
                        lines[i][k].lifes += 1
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Игровое поле')
window.fill((0, 0, 0))

x_length = 1000/c
y_length = x_length
class Reect():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, x_length, y_length)
        pygame.draw.rect(window, (0, 0, 0), self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def paint(self, live):
        if live:
            pygame.draw.rect(window, (255, 0, 155), self.rect)
        else:
            pygame.draw.rect(window, (0, 0, 0), self.rect)
rects = list()

for i in range(c):
    line = list()
    y = i*1000/c
    for k in range(c):
        x = k*1000/c
        line.append(Reect(x, y))
    rects.append(line)
    pygame.display.update()

wait = 1

lines = list()
class Cell():
    def __init__(self, value, lifes):
        self.value = value
        self.lifes = lifes

for i in range(c):
    line = list()
    for k in range(c):
        line.append(Cell(0, 0))
    lines.append(line)

button = 0
buttondown = 0
while wait:
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            button = (i.button-3)//-2
            x, y = i.pos
            for a in range(c):
                for b in range(c):
                    if rects[a][b].collidepoint(x, y):
                        lines[a][b].value = button
                        rects[a][b].paint(button)
            buttondown = 1
        if i.type == pygame.MOUSEMOTION and buttondown:
            m, k = i.pos
            for a in range(c):
                for b in range(c):
                    if width == 1:
                        if rects[a][b].collidepoint(m, k):
                            rects[a][b].paint(button)
                            lines[a][b].value = button
                    else:
                        if rects[a][b].collidepoint(m, k):
                            a_max = a + width/2
                            a_min = a-width/2
                            b_min = b - width/2
                            b_max = b+ width/2
                            if a + width/2 > c-1:
                                a_max = c
                            if a-width/2 < 0:
                                a_min = 0
                            if b+width/2 > c-1:
                                b_max = c
                            if b-width/2 < 0:
                                b_min = 0
                            
                            
                            for d in range(int(a_min), int(a_max)):
                                for e in range(int(b_min), int(b_max)):
                                    lines[d][e].value = 1
                                    rects[d][e].paint(button)
        if i.type == pygame.MOUSEBUTTONUP:
            buttondown = 0
        if i.type == pygame.KEYDOWN:
            if i.key == 13:
                wait = 0
            elif i.key ==27:
                wait = 0
                game = 0
            elif i.key == 1073741906:
                width = width + 1
            elif i.key == 1073741905:
                if width != 0:
                    width = width - 1
        if i.type == pygame.QUIT:
            wait = 0
            game = 0
        pygame.display.update()


while game == 1:
    for i in range(c):
        for k in range(c):
            for b in range(i-1, i+2):
                for a in range(k-1, k+2):
                    if b == i and a == k:
                        pass
                    elif lines[int(b%c)][int(a%c)].value == 1:
                        lines[i][k].lifes += 1
            
    for i in range(c):
        for k in range(c):
            if lines[i][k].lifes == 3:
                lines[i][k].value = 1
                live = 1
                rects[i][k].paint(live)
            elif lines[i][k].lifes == 2 and lines[i][k].value == 1:
                lines[i][k].value = 1
                live = 1
                rects[i][k].paint(live)
            else:
                lines[i][k].value = 0
                live = 0
                rects[i][k].paint(live)
            lines[i][k].lifes = 0

    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = 0
        if i.type == pygame.KEYDOWN:
            if i.key == 27:
                game = 0
    
    clock.tick(20)

