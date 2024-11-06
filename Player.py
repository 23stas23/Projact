import pygame
from random import randint
import sys

# Инициализация Pygame
pygame.init()

# Настройка окна
WIDTH = 1000
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm")
clock = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)

FPS = 60

all_sprites = pygame.sprite.Group()
fence_group = []
hand = True
hand_open = True


tools_group_equp =["Hand", "Axe"]
tools = {"Hand":{"image":BLACK},"Axe":{"image": (100, 100, 100)}}


class Player(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.tool = 0
        self.image = pygame.Surface((60, 70))
        self.image = pygame.transform.scale(pygame.image.load("Image/Player.png"), (60, 70))
        self.rect = self.image.get_rect(center = (500, 400))
    
    def update(self):
        screen.blit(self.image, self.rect)
    def moving(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            for fence in fence_group:
                if self.rect.colliderect(fence):
                    self.rect.x += self.speed
                    break
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            for fence in fence_group:
                if self.rect.colliderect(fence):
                    self.rect.x -= self.speed
                    break
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            for fence in fence_group:
                if self.rect.colliderect(fence):
                    self.rect.y += self.speed
                    break
        if keys[pygame.K_s]:
            self.rect.y += self.speed
            for fence in fence_group:
                if self.rect.colliderect(fence):
                    self.rect.y -= self.speed
                    break
        

    def change_tools(self):
        global tools_group_equp
        if self.tool > 1:
            self.tool = 0
        name = tools_group_equp[self.tool]

        
        
            
            

player = Player(3)
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
            player.tool += 1
    screen.fill(BLACK)
    player.update()
    player.moving()
    player.change_tools()
    pygame.display.flip()

    print(player.tool)
    
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
