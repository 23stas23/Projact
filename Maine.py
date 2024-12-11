import pygame
import sys

from Player import *
from Market import *
from Inventory import *


from random import randint

pygame.init()
    
WIDTH = 1000
HEIGHT = 500
FPS = 60
    
BLACK = (0, 0, 0)
WHITE = (150, 150, 150)
    
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm")
clock = pygame.time.Clock()

player = Player(5)

maket()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(BLACK)
    #Player
    screen.blit(player.image, player.rect)
    player.moving()

    #Markt
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
sys.exit()
