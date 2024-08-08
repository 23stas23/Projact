import pygame
import sqlite3
from random import randint
import sys

# Подключение к базе данных
conn = sqlite3.connect('Inventory.db')
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''CREATE TABLE IF NOT EXISTS Inventory (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, counts INTEGER NOT NULL)''')

# Функция для получения текущего значения counts по имени
def get_count(name):
    cursor.execute("SELECT counts FROM Inventory WHERE name = ?", (name,))
    result = cursor.fetchone()
    return result[0] if result else None

# Функция для обновления значения counts по имени
def update_count(name, new_count):
    cursor.execute("SELECT id FROM Inventory WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        cursor.execute("UPDATE Inventory SET counts = ? WHERE name = ?", (new_count, name))
    else:
        cursor.execute("INSERT INTO Inventory (name, counts) VALUES (?, ?)", (name, new_count))
    conn.commit()

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

#Seting game
all_sprites = pygame.sprite.Group()
all_item = pygame.sprite.Group()
ToolsPlayer = pygame.sprite.Group()
all_UIsprites = pygame.sprite.Group()
#items
items = {"Apple": {"id": 1, "name":"Apple", "image":"Image/Appal.png", "cost": 50}, "Wood":{"id": 2, "name": "Wood", "image": "Image/Wood.png", "cost": 100}, "Axe": {"id": 1, "name": "Axe", "image": "Image/Axe.png", "cost": 150}}
coins = 150
level_player = 0
progras_level = 0
AppleCount = get_count("Apple")
WoodCount = get_count("Wood")

def bacgraund():
    bacgraund_image = pygame.transform.scale(pygame.image.load("Image/BackGraund.png"), (WIDTH, HEIGHT))
    bacgraund_rect = bacgraund_image.get_rect()
    screen.blit(bacgraund_image, bacgraund_rect)

#List sprites

#Player
class Player(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.Surface((60, 70))
        self.image = pygame.transform.scale(pygame.image.load("Image/Player.png"), (60, 70))
        self.rect = self.image.get_rect(center = (500, 400))
    
    #def change_tools(self):
        
    def update(self):
        screen.blit(self.image, self.rect)
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
player = Player(3)
all_sprites.add(player)

#tools item seting 
class tools_player(pygame.sprite.Sprite): 
    def __init__(self, name, open, width, height, x, y, num_slot, active ):
        super().__init__()
        self.name = name
        self.open = open 
        self.num_slot = num_slot
        self.active = active 

        self.image = pygame.transform.scale(pygame.image.load(items[str(self.name)]["image"]), (width, height))
        self.rect = self.image.get_rect(topleft = (player.rect.x + x, player.rect.y + y))
    def update(self):
        if self.active:
            screen.blit(self.image, self.rect)
    def event_buttone(self):
        if self.open:
            if self.active:
                self.active = False 
            else: 
                self.active = True

Axe_open = False
Axe_active =False

#Level
num_level = 0
bar_level = progras_level

class Bar(pygame.sprite.Sprite):
    def __init__(self, x, y, font, text, text_num, level):
        super().__init__()
        #Background Bar
        self.backgroundBar_image = pygame.transform.scale(pygame.image.load("Image/UI_BacgraundLevel.png"), (150, 30))
        self.backgroundBar_rect = self.backgroundBar_image.get_rect( topleft = (x, y))
        #Bar
        self.bur = 90
        self.size = 140*level
        self.Bur_image = pygame.transform.scale(pygame.image.load("Image/UI_LevelBar.png"), (self.size, 28))
        self.Bur_rect = self.Bur_image.get_rect(topleft = (self.backgroundBar_rect.x + 2.5, self.backgroundBar_rect.y + 2.5))

        #Text Bar
        self.Bur_text = font.render(f"{text} {text_num}", True, WHITE)
    def update(self):
        screen.blit(self.backgroundBar_image, self.backgroundBar_rect)
        screen.blit(self.Bur_image, self.Bur_rect)
        screen.blit(self.Bur_text, (75, 15))
    def event_button(self):
        pass
Level_bars = Bar(10, 10, font1, "Lvl:", num_level, bar_level)
all_sprites.add(Level_bars)
        
class Items(pygame.sprite.Sprite):
    def __init__(self, x, y, name, count, active):
        super().__init__()
        self.name = name 
        self.count = count
        self.active = active
        self.item_image = pygame.transform.scale(pygame.image.load(items[str(self.name)]["image"]), (40, 40))
        self.item_rect = self.item_image.get_rect(center = (x, y))
    def update(self): 
        if self.active:
            screen.blit(self.item_image, self.item_rect)
        if self.active and player.rect.colliderect(self.item_rect):
            self.count += randint(1, 5)
            update_count(self.name, self.count)
            print(get_count(self.name))
            self.active = False



all_item = pygame.sprite.Group()
apple = Items(400, 400, "Apple", AppleCount, True) 
all_item.add(apple)

#CoinsUI
class UI_Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.coins_image = pygame.transform.scale(pygame.image.load("Image/Coins.png"), (40, 40))
        self.coins_rect = self.coins_image.get_rect(topleft = (WIDTH - 90, 10))
    def update(self):
        global coins
        self.text = font.render(f"{coins}", True, WHITE)
        screen.blit(self.coins_image, self.coins_rect)
        screen.blit(self.text, (self.coins_rect.x +50, 10))

coinsUI = UI_Coins()
all_UIsprites.add(coinsUI)

#UI BackgroundUI
class UI_Background(pygame.sprite.Sprite):
    def __init__(self, x, y, active):
        super().__init__()
        self.active = active
        self.UI_image= pygame.transform.scale(pygame.image.load("Image/UI_Inventory.png"), (750, 500))
        self.UI_rect = self.UI_image.get_rect(topleft = (x, y))
    def backgroundUI(self):
        if self.active:
            screen.blit(self.UI_image, self.UI_rect)

#Inventory
InventoryActive = False
inventory = UI_Background(100, 100, InventoryActive)
all_UIsprites.add(inventory)

#Inventory slot
class UI_Inventory_slot(pygame.sprite.Sprite):
    def __init__(self, x, y, item, font, count):
        super().__init__()
        
        self.font = font
        self.item = item
        self.count = count
        #slot inventory
        self.slot_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (80, 80))
        self.slot_rect = self.slot_image.get_rect(topleft = (100 + x, 100+ y))
        #item inventory
        self.item_image = pygame.transform.scale(pygame.image.load(str(items[item]["image"])), (70, 70))
        self.item_rect = self.item_image.get_rect(topleft = (self.slot_rect.x + 5, self.slot_rect.y + 5))
        #item name inventory
        self.name_item = self.font.render(str(items[self.item]["name"]), True, WHITE)

    def update(self):
        global AppleCount, WoodCount
        if InventoryActive:
            screen.blit(self.slot_image, self.slot_rect)
            screen.blit(self.item_image, self.item_rect)
            screen.blit(self.name_item, (self.slot_rect.x + 15, self.slot_rect.y + 75))
            #item count inventory
            self.count_item = self.font.render(str(self.count), True, WHITE)
            screen.blit(self.count_item, (self.slot_rect.x + 65, self.slot_rect.y + 50))

            AppleCount = get_count("Apple")
            WoodCount = get_count("Wood")
            cursor.execute("SELECT * FROM Inventory")
            rows = cursor.fetchall()
            # Выводим данные
            for row in rows:
                print(row)
            
#number slots
slot = UI_Inventory_slot(10, 10, "Apple", font1, AppleCount)
slot1 = UI_Inventory_slot(100, 10, "Wood", font1, WoodCount)

all_UIsprites.add(slot, slot1)

#UI Market 
Market_active = False
market = UI_Background(100, 100, Market_active)
all_UIsprites.add(market)

class UI_Market_slot(pygame.sprite.Sprite):
    def __init__(self, x, y, item, active, font):
        super().__init__()
        self.active = active
        self.font = font
        self.item = item
        
        self.slot_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (80,80))
        self.slot_rect = self.slot_image.get_rect(topleft = (100 + x, 100 + y))

        self.item_image = pygame.transform.scale(pygame.image.load(str(items[self.item]["image"])), (65,65))
        self.item_rect = self.item_image.get_rect(topleft = (self.slot_rect.x + 5, self.slot_rect.y + 5))

        self.button_image = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png"), (80, 20))
        self.button_rect = self.button_image.get_rect(topleft = (self.slot_rect.x, self.slot_rect.y + 75))

        self.cost_item_text = font1.render(str(items[self.item]["cost"]), True, WHITE)
    def update(self):
        if Market_active:
            screen.blit(self.slot_image, self.slot_rect)
            screen.blit(self.item_image, self.item_rect)
            screen.blit(self.button_image, self.button_rect)
            screen.blit(self.cost_item_text, (self.slot_rect.x + 55, self.slot_rect.y + 50))
    def event_button(self):
        if InventoryActive == False and Market_active == False:
            Market_active = True
        else:
            Market_active = False
    def event_bayItem(self):
        global coins
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if Market_active:
            if self.button_rect.collidepoint(mouse_pos) and mouse_click[0]:  # Left mouse button is pressed
                self_cost = items[self.item]["cost"]
                if coins >= self_cost:
                    coins -= self_cost
                    self.active = True


#number slots
market_slot = UI_Market_slot(20, 20, "Axe", Market_active, font1)
market_slot1 = UI_Market_slot(120, 20, "Apple", Market_active, font1)

all_UIsprites.add(market_slot, market_slot1)

#garden
timer = 0
fence_group = []
class Garden(pygame.sprite.Sprite):
    def __init__(self, x, y, gardenActive, grow_open):
        super().__init__()
        self.active = gardenActive
        self.open = grow_open
        
        self.image = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
        self.rect = self.image.get_rect(topleft = (x, y))

        self.sead_image =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
        self.sead_rect = self.sead_image.get_rect(topleft = (self.rect.x + 5, self.rect.y + 5))

        self.StartTree_image = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
        self.StartTree_rect = self.StartTree_image.get_rect(topleft = (self.rect.x + 5, self.rect.y - 30))

        self.FinishTree_image = pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
        self.FinishTree_rect = self.FinishTree_image.get_rect(topleft = (self.rect.x + 5, self.rect.y - 40))

        self.ApelTree_image = pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
        self.ApelTree_rect = self.ApelTree_image.get_rect(topleft = (self.rect.x + 5, self.rect.y - 40))

        self.fence_image = pygame.transform.scale(pygame.image.load("Image/image.png"), (120, 120))
        self.fence_rect = self.fence_image.get_rect(topleft = (self.rect.x -25, self.rect.y- 25  ))

        fence_group.append(self.fence_rect)

    def update(self):
        global timer
        screen.blit(self.image, self.rect)
        self.timer = timer
        if self.active and self.open:
            if self.timer >=0 and self.timer <= 5:
                screen.blit(self.sead_image, self.sead_rect)
            if self.timer >= 5 and self.timer <= 10:
                screen.blit(self.StartTree_image, self.StartTree_rect)

            if self.timer >= 10 and self.timer <= 15:
                screen.blit(self.FinishTree_image, self.FinishTree_rect)
            if self.timer >= 15:
                screen.blit(self.ApelTree_image, self.ApelTree_rect)
        if self.open :
            screen.blit(self.fence_image, self.fence_rect)
    def event_button(self):
        global timer
        if self.open and self.active == False and player.rect.colliderect(self.rect):
            self.active = True
            timer = 0
        if self.open and self.active and player.rect.colliderect(self.rect) and self.timer >=15:
            self.active = False
#Gardens
garden = Garden(100, 500, False, False)
all_sprites.add(garden)

        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                garden.event_button()
            if event.key == pygame.K_i:
                if InventoryActive == False and Market_active == False:
                    InventoryActive = True
                else:
                    InventoryActive = False
            if event.key == pygame.K_m:
                if InventoryActive == False and Market_active == False:
                    Market_active = True
                else:
                    Market_active = False
            if event.key == pygame.K_1:
                Axe.event_buttone()
        #if event.type == pygame.MOUSEBUTTONDOWN:
            



    screen.fill(BLACK)
    inventory = UI_Background(100, 100, InventoryActive)
    market = UI_Background(100, 100, Market_active)
    all_UIsprites.add(market)
    all_UIsprites.add(inventory)

    bacgraund()
    #Player render
    screen.blit(player.image, player.rect)
    player.update()
    
    #Tools
    Axe = tools_player("Axe", Axe_open, 35, 30, 20, 5, 1, Axe_active )
    ToolsPlayer.add(Axe)

    #UI all_sprits
    all_sprites.update()
    ToolsPlayer.update()

    all_item.update()

    #render UIsprits
    inventory.backgroundUI()
    market.backgroundUI()
    all_UIsprites.update()

    #event bay item
    market_slot.event_bayItem()
    market_slot1.event_bayItem()

    #timers
    timer += 1/FPS
    print(coins)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
