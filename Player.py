import pygame
from random import randint
import sys

pygame.init()
    
WIDTH = 1000
HEIGHT = 500
FPS = 60
    
BLACK = (0, 0, 0)
WHITE = (150, 150, 150)
    
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
fence_group = []
hand = True
hand_open = True

font = pygame.font.SysFont("Arial", 32)
font1 =pygame.font.SysFont("Arial", 22)

items = {"Apple": {"id": 1, "name":"Apple", "image":"Image/Appal.png", "cost": 50}, "Wood":{"id": 2, "name": "Wood", "image": "Image/Wood.png", "cost": 100}, "Axe": {"id": 1, "name": "Axe", "image": "Image/Axe.png", "cost": 150}}


tools_group_equp =["Hand", "Axe"]
tools = {"Hand":{"image":"Image/Appel.png"},"Axe":{"image": "Image/Axe.png"}}

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
        rect_tool.x = player.rect.x + 10
        rect_tool.y = player.rect.y + 10
        screen.blit(image_tool, rect_tool)
        
player = Player(3)
all_sprites.add(player)

#_____________________Inventory__________________________
class Inventory(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Active = False
        self.image = pygame.transform.scale(pygame.image.load("Image/UI_Inventory.png"), (700, 400))
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = 70
    def update(self):
        if self.Active:
            screen.blit(self.image, self.rect)
        
            
        
        
inventory = Inventory()
#________________________________________Slot_Inventory_________________________________________
class Slot(pygame.sprite.Sprite):
    def __init__(self, direction_x, direction_y, name, count):
        super().__init__()
        self.x = direction_x
        self.y = direction_y
        self.h = 55
        self.w = 55
        self.name = name
        self.count = count

        self.image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (self.h, self.w))
        self.rect = self.image.get_rect()
        self.rect.x = inventory.rect.x + self.x
        self.rect.y = inventory.rect.y + self.y

        self.item_image = pygame.transform.scale(pygame.image.load(items[self.name]["image"]), (self.h-5, self.w-5))
        self.item_rect = self.item_image.get_rect()
        self.item_rect.x = self.rect.x + 2.5
        self.item_rect.y = self.rect.y + 2.5

        
    def update(self):
        self.count_item = pygame.transform.scale(font.render(str(self.count), True, WHITE), (20, 24))
        if inventory.Active:
            screen.blit(self.image, self.rect)
            screen.blit(self.item_image, self.item_rect)
            screen.blit(self.count_item, (self.rect.x + 35, self.rect.y + 35))
slot = Slot(20, 20, "Apple", 00)

#________________________Market_______________________
class Market(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.Active = False
        #Create background Inventory 
        self.image = pygame.transform.scale(pygame.image.load("Image/UI_Inventory.png"), (700, 400))
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = 70
    def update(self):
        if self.Active:
            screen.blit(self.image, self.rect)

        
            
        
        
market = Market()
#________________________________________Slot_Market_________________________________________
class Market_Slot(pygame.sprite.Sprite):
    def __init__(self, direction_x, direction_y, name, count):
        super().__init__()
        #Seting Slot
        self.x = direction_x
        self.y = direction_y
        self.h = 55
        self.w = 55
        self.name = name
        self.count = count

        #Create Image slot
        self.image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (self.h, self.w))
        self.rect = self.image.get_rect()
        self.rect.x = inventory.rect.x + self.x
        self.rect.y = inventory.rect.y + self.y

        #create Item Image
        self.item_image = pygame.transform.scale(pygame.image.load(items[self.name]["image"]), (self.h-5, self.w-5))
        self.item_rect = self.item_image.get_rect()
        self.item_rect.x = self.rect.x + 2.5
        self.item_rect.y = self.rect.y + 2.5

        #Create buttone
        self.buttone = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png", (self.h, 20)))
        self.buttone_rect = self.buttone.get_rect()
        self.buttone_rect.x = self.h + 5
        self.buttone_rect.y = self.w + 5

        
    def update(self):
        self.count_item = pygame.transform.scale(font.render(str(self.count), True, WHITE), (20, 24))
        if market.Active:
            screen.blit(self.image, self.rect)
            screen.blit(self.item_image, self.item_rect)
            screen.blit(self.count_item, (self.rect.x + 35, self.rect.y + 35))
m_slot = Slot(20, 20, "Apple", 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                player.tool += 1
            if event.key == pygame.K_e:
                if inventory.Active:
                    inventory.Active = False
                else:
                    if market.Active == False:
                        inventory.Active = True
            if event.key == pygame.K_m:
                if market.Active:
                    market.Active = False
                else:
                    if inventory.Active == False:
                        market.Active = True
    screen.fill(BLACK)
    #Player setings
    player.update()
    player.moving()
    player.change_tools()
    #Inventory setings
    inventory.update()
    slot.update()
    #Market setings
    market.update()
    m_slot.update()
    
    pygame.display.flip()

    print(player.tool)
    
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
