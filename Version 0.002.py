import pygame
from random import randint
import sys

# Инициализация Pygame
pygame.init()

# Настройка окна
WIDTH = 1000
HEIGHT = 800
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

def bacgraund():
    bacgraund_image = pygame.transform.scale(pygame.image.load("Image/BackGraund.png"), (WIDTH, HEIGHT))
    bacgraund_rect = bacgraund_image.get_rect()
    bacgraund_rect.x = 0
    bacgraund_rect.y = 0
    screen.blit(bacgraund_image, bacgraund_rect)

#List sprites
all_sprites = pygame.sprite.Group()

#items
items = {"apple": {"id": 1, "name":"Apple", "image":"Image/Appal.png", "cost": 50, "count": 0}, "wood":{"id": 2, "name": "Wood", "image": "Image/Wood.png", "cost": 100, "count": 0}, "axe": {"id": 1, "name": "Axe", "image": "Image/Axe.png", "cost": 50}}

#Player
up_move = False
down_move = False
right_move =False
left_move = False
speed_player = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #player
        self.image = pygame.Surface((60, 70))
        self.image = pygame.transform.scale(pygame.image.load("Image/Player.png"), (60, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        
    def update(self):
        screen.blit(self.image, self.rect)
    def event_button(self, event):
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.rect.x -= speed_player
            if event.key == pygame.K_d:
                self.rect.x += speed_player
            if event.key == pygame.K_w:
                self.rect.y -= speed_player
            if event.key == pygame.K_s:
                self.rect.y += speed_player
player = Player()
all_sprites.add(player)

#garden
garden_active = False
grow = False
timer = 0
class Garden(pygame.sprite.Sprite):
    def __init__(self, x, y, gardenActive):
        super().__init__()
        self.active = gardenActive
        
        self.image = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.sead_image =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
        self.sead_rect = self.sead_image.get_rect()
        self.sead_rect.x = self.rect.x + 5
        self.rect.y = self.rect.y + 5

        self.StartTree_image = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
        self.StartTree_rect = self.StartTree_image.get_rect()
        self.StartTree_rect.x = self.rect.x + 5
        self.StartTree_rect.y = self.rect.y - 30

        self.FinishTree_image = pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
        self.FinishTree_rect = self.FinishTree_image.get_rect()
        self.FinishTree_rect.x = self.rect.x + 5
        self.FinishTree_rect.y = self.rect.y - 40

        self.ApelTree_image = pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
        self.ApelTree_rect = self.ApelTree_image.get_rect()
        self.ApelTree_rect.x = self.rect.x + 5
        self.ApelTree_rect.y = self.rect.y - 40
    def update(self):
        screen.blit(self.image, self.rect)
        if grow and self.active:
            if timer >=0 and timer <= 5:
                screen.blit(self.sead_image, self.sead_rect)
            if timer >= 5 and timer <= 10:
                screen.blit(self.StartTree_image, self.StartTree_rect)

            if timer >= 10 and timer <= 15:
                screen.blit(self.FinishTree_image, self.FinishTree_rect)
            if timer >= 15:
                screen.blit(self.ApelTree_image, self.ApelTree_rect)
    def event_button(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and player.rect.colliderect(self.rect) and grow == False and self.active:
                grow = True
                timer = 0
            if event.key == pygame.K_e and player.rect.colliderect(self.rect) and grow and self.active == False:
                grow = False
                
#Gardens
garden = Garden(100, 500, True)
all_sprites.add(garden)


#Level
num_level = 0
bar_level = 0.5

class Bar(pygame.sprite.Sprite):
    def __init__(self, x, y, font, text, text_num, level):
        super().__init__()
        #Background Bar
        self.backgroundBar_image = pygame.transform.scale(pygame.image.load("Image/UI_BacgraundLevel.png"), (150, 30))
        self.backgroundBar_rect = self.backgroundBar_image.get_rect()
        self.backgroundBar_rect.x = x
        self.backgroundBar_rect.y = y
        #Bar
        self.bur = 90
        self.size = 140*level
        self.Bur_image = pygame.transform.scale(pygame.image.load("Image/UI_LevelBar.png"), (self.size, 28))
        self.Bur_rect = self.Bur_image.get_rect()
        self.Bur_rect.x = self.backgroundBar_rect.x + 2.5
        self.Bur_rect.y = self.backgroundBar_rect.y + 2.5
        #Text Bar
        self.Bur_text = font.render(f"{text} {text_num}", True, WHITE)
    def update(self):
        screen.blit(self.backgroundBar_image, self.backgroundBar_rect)
        screen.blit(self.Bur_image, self.Bur_rect)
        screen.blit(self.Bur_text, (155, 15))
    def event_button(self, event):
        pass
Level_bars = Bar(10, 10, font1, "Lvl:", num_level, bar_level)
all_sprites.add(Level_bars)
        
class Coins(pygame.sprite.Sprite):
    def __init__(self, x, y, font):
        #Coins
        self.coins_image = pygame.transform.scale(pygame.image.load("Image/Coins.png"), (40, 40))
        self.coins_rect = self.coins_image.get_rect()
        self.coin_rect.x = 10
        self.coin_rect.y = 40
    def event_button(self, event):
        pass
        

#UI Inventory
InventoryActive = False

UI_Inventory_image = pygame.transform.scale(pygame.image.load("Image/UI_Inventory.png"), (750, 500))
UI_Inventory_rect = UI_Inventory_image.get_rect()
UI_Inventory_rect.x = 100
UI_Inventory_rect.y = 100

#Inventory slot
class UI_Inventory_slot(pygame.sprite.Sprite):
    def __init__(self, x, y, item, actives, font):
        super().__init__()
        
        self.active = actives
        self.font = font
        self.item = item
        #slot inventory
        self.slot_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (80, 80))
        self.slot_rect = self.slot_image.get_rect()
        self.slot_rect.x = UI_Inventory_rect.x + x
        self.slot_rect.y = UI_Inventory_rect.y + y
        #item inventory
        self.item_image = pygame.transform.scale(pygame.image.load(str(items[item]["image"])), (70, 70))
        self.item_rect = self.item_image.get_rect()
        self.item_rect.x = self.slot_rect.x + 5
        self.item_rect.y = self.slot_rect.y + 5
        #item name inventory
        self.name_item = self.font.render(str(items[self.item]["name"]), True, WHITE)

    def update(self):
        if InventoryActive:
            screen.blit(self.slot_image, self.slot_rect)
            screen.blit(self.item_image, self.item_rect)
            screen.blit(self.name_item, (self.slot_rect.x + 15, self.slot_rect.y + 75))
            #item count inventory
            self.count_item = self.font.render(str(items[self.item]["count"]), True, WHITE)
            screen.blit(self.count_item, (self.slot_rect.x + 65, self.slot_rect.y + 50))
    def event_button(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i and InventoryActive == False and Market_active == False:
                InventoryActive = True
            else:
                InventoryActive = False
            
#number slots
slot = UI_Inventory_slot(10, 10, "apple", InventoryActive, font1)
slot1 = UI_Inventory_slot(100, 10, "wood", InventoryActive, font1)

all_sprites.add(slot, slot1)

#Market
Market_active = False

#UI Market 
UI_Market_image = pygame.transform.scale(pygame.image.load("Image/UI_inventory.png"), (750, 500))
UI_Market_rect = UI_Market_image.get_rect()
UI_Market_rect.x = 100
UI_Market_rect.y = 100

class UI_Market_slot(pygame.sprite.Sprite):
    def __init__(self, x, y, item, active, font):
        super().__init__()
        self.active = active
        self.font = font
        self.item = item
        
        self.slot_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (80,80))
        self.slot_rect = self.slot_image.get_rect()
        self.slot_rect.x = UI_Market_rect.x + x
        self.slot_rect.y = UI_Market_rect.y + y

        self.item_image = pygame.transform.scale(pygame.image.load(str(items[self.item]["image"])), (70,70))
        self.item_rect = self.item_image.get_rect()
        self.item_rect.x = self.slot_rect.x + 5
        self.item_rect.y = self.slot_rect.y + 5

        self.button_image = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png"), (80, 20))
        self.button_rect = self.button_image.get_rect()
        self.button_rect.x = self.slot_rect.x
        self.button_rect.y = self.slot_rect.y + 75

        self.cost_item_text = font1.render(str(items[self.item]["cost"]), True, WHITE)
    def update(self):
        if Market_active:
            screen.blit(self.slot_image, self.slot_rect)
            screen.blit(self.item_image, self.item_rect)
            screen.blit(self.button_image, self.button_rect)
            screen.blit(self.cost_item_text, (self.slot_rect.x + 55, self.slot_rect.y + 50))
    def event_button(self, event):
        if event.type == pygame.KEYDOWN:
            #Market Open
            if event.key == pygame.K_m and InventoryActive == False and Market_active == False:
                Market_active = True
            else:
                Market_active = False

#number slots
market_slot = UI_Market_slot(20, 20, "axe", Market_active, font1)
market_slot1 = UI_Market_slot(120, 20, "apple", Market_active, font1)

all_sprites.add(market_slot, market_slot1)

        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.event_button()

    screen.fill(BLACK)
    bacgraund()
    #Player render
    screen.blit(player.image, player.rect)
    player.update()
    #UI Inventory render
    if InventoryActive:
        screen.blit(UI_Inventory_image, UI_Inventory_rect)
    #UI Market render
    if Market_active:
        screen.blit(UI_Market_image, UI_Market_rect)
    #UI all_sprits
    all_sprites.update()
    #timers
    timer += 1/60

    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
