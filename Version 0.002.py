import pygame
from random import randint
import sys

# Инициализация Pygame
pygame.init()

# Настройка окна
WIDTH = 200
HEIGHT = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm")
clock = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (25, 25, 255)
GRAY = (127,140,140)
GREEN = (0, 255, 17)
FPS = 60
font = pygame.font.SysFont("Arial", 32)
font1 =pygame.font.SysFont("Arial", 22)

#Player
up_move = False
down_move = False
right_move =False
left_move = False
speed_player = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 70))
        self.image = pygame.image.load("Image/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        
    def update(self):
        screen.blit(self.image, self.rect)
        if up_move:
            Player_rect.y -= speed_player

        if down_move:
            Player_rect.y += speed_player

        if right_move:
            Player_rect.x += speed_player

        if left_move:
            Player_rect.x -= speed_player
player = Player()

class UI_Inventory_slot(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("Image/UI_Inventory.png"), (750, 500))
        self.rect = UI_Inventory_image.get_rect(100, 100)
    #def update(self):
        
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    player.update()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
