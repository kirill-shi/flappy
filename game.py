#импорт модуля
import pygame
import sys
from pygame.locals import QUIT

pygame.init()

# опр основных свойств игры 
FPS = 60
Frames = pygame.time.Clock()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

BACKGROUND_COLOR = (25, 25, 150)

# иницизизайия графического интерфейса
pygame.display.set_caption('Flappy bird')

screen_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#cущность игры

class Bird:
    def __init__(self) -> None:
        #тут описываем свойства птицы
        self.image = pygame.image.load('ima.png')
        self.rect = self.image.get_rect()

#ДВИЖОК

while True:
    #1) выйти из движка 2) повторяемые операции 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # блок обноления 

    #Блок отрисовки объектов
    screen_surface.fill(BACKGROUND_COLOR)
    pygame.display.update()    
    Frames.tick(FPS)