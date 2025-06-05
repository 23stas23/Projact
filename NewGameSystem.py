import pygame, random, math, sys, os, time


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
WHITE = (255, 255, 255)
BLUE = (25, 25, 255)
GRAY = (127,140,140)
GREEN = (0, 255, 17)
FPS = 60
font = pygame.font.SysFont("Arial", 32)
font1 =pygame.font.SysFont("Arial", 22)





all_sprites = pygame.sprite.Group()
fence_group = []
hand = True
hand_open = True

items = {"Apple": {"id": 1, "name":"Apple", "image":"Image/Appal.png", "cost": 50}, "Wood":{"id": 2, "name": "Wood", "image": "Image/Start_tree.png", "cost": 100}, "Axe": {"id": 1, "name": "Axe", "image": "Image/Axe.png", "cost": 150}}


tools_group_equp =["Hand", "Axe"]
tools = {"Hand":{"image":"Image/Appal.png"},"Axe":{"image": "Image/Axe.png"}}

#________________Player__________________#
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
        name = ""
        name = tools_group_equp[int(self.tool)]
        image_tool = pygame.transform.scale(pygame.image.load(tools[name]["image"]), (20, 20))
        rect_tool = image_tool.get_rect()
        rect_tool.x = self.rect.x + 10
        rect_tool.y = self.rect.y + 10
        screen.blit(image_tool, rect_tool)
        




running = True
while running:
    for event in pygame.event.get():
        Player(2).moving()
    screen.fill(BLACK)
    Player(2).update()
    
    

    
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()
