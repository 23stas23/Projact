import pygame
from random import randint
import sys

# Инициализация Pygame
pygame.init()

# Настройка окна
WIDTH = 1000
HEIGHT = 980
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
        self.image = pygame.Surface((60, 70))
        self.image = pygame.transform.scale(pygame.image.load("Image/Player.png"), (60, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= speed_player
        if keys[pygame.K_d]:
            self.rect.x += speed_player
        if keys[pygame.K_w]:
            self.rect.y -= speed_player
        if keys[pygame.K_s]:
            self.rect.y += speed_player
player = Player()

#UI Inventory
InventoryActive = False
Inventory_slots = pygame.sprite.Group()

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

        self.slot_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (80, 80))
        self.slot_rect = self.slot_image.get_rect()
        self.slot_rect.x = UI_Inventory_rect.x + x
        self.slot_rect.y = UI_Inventory_rect.y + y

        self.item_image = pygame.transform.scale(pygame.image.load(str(items[item]["image"])), (70, 70))
        self.item_rect = self.item_image.get_rect()
        self.item_rect.x = self.slot_rect.x + 5
        self.item_rect.y = self.slot_rect.y + 5

        self.name_item = self.font.render(str(items[self.item]["name"]), True, WHITE)

    def update(self):
        if InventoryActive:
            screen.blit(self.slot_image, self.slot_rect)
            screen.blit(self.item_image, self.item_rect)
            screen.blit(self.name_item, (self.slot_rect.x + 15, self.slot_rect.y + 75))
            
            self.count_item = self.font.render(str(items[self.item]["count"]), True, WHITE)
            screen.blit(self.count_item, (self.slot_rect.x + 65, self.slot_rect.y + 50))
            
#number slots
slot = UI_Inventory_slot(10, 10, "apple", InventoryActive, font1)
slot1 = UI_Inventory_slot(100, 10, "wood", InventoryActive, font1)

Inventory_slots.add(slot, slot1)

#Market
Market_active = False
Market_slots =  pygame.sprite.Group()

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
        
        self.slot_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (70,70))
        self.slot_rect = self.slot_image.get_rect()
        self.slot_rect.x = UI_Market_rect.x + x
        self.slot_rect.y = UI_Market_rect.y + y

        self.item_image = pygame.transform.scale(pygame.image.load("Image/Axe.png"), (50,50))
        self.item_rect = self.item_image.get_rect()
        self.item_rect.x = self.slot_rect.x + 5
        self.item_rect.y = self.slot_rect.y + 5

        self.button_image = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png"), (70, 20))
        self.button_rect = self.button_image.get_rect()
        self.button_rect.x = self.slot_rect.x
        self.button_rect.y = self.slot_rect.y + 75

        self.cost_item_text = font1.render(str(items[self.item]["cost"]), True, WHITE)
    def update():
        if Market_active:
            screen.blit(self.slot_image, self.slot.rect)
            screen.blit(self.item_image, self.item_rect)
            screen.blit(self.button_image, self.button_rect)
            screen.blit(self.cost_item_text, (self.slot_rect2.x + 55, self.slot_rect.y + 50))

#number slots
market_slot = UI_Market_slot(20, 20, "axe", Market_active, font1)
market_slot1 = UI_Market_slot(120, 20, "apple", Market_active, font1)

Market_slots.add(market_slot, market_slot1)

        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and InventoryActive == False and Market_active == False:
                InventoryActive = True
            else:
                InventoryActive = False
            if event.key == pygame.K_m and InventoryActive == False and Market_active == False:
                Market_active = True
            else:
                Market_active = False

    screen.fill(BLACK)
    bacgraund()
    #Player render
    screen.blit(player.image, player.rect)
    player.update()
    #UI Inventory render
    if InventoryActive:
        screen.blit(UI_Inventory_image, UI_Inventory_rect)
    Inventory_slots.update()

    #UI Market render
    if Market_active:
        screen.blit(UI_Market_image, UI_Market_rect)
    Market_slots.update()
    

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
