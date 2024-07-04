import pygame
from random import randint
import sys

# Инициализация Pygame
pygame.init()

# Настройка окна
WIDTH = 1500
HEIGHT = 1000
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

#Closers Gardens
closers_gardens = [] 

#Player 
Player_image = pygame.transform.scale(pygame.image.load("Image/Player.png"), (60, 70))
Player_rect = Player_image.get_rect()
Player_rect.x = WIDTH//2
Player_rect.y = HEIGHT//2

#Player moving
up_move = False
down_move = False
right_move =False
left_move = False
speed_player = 5

def moving_player():
    global Player_rect, Axe_rect
    if up_move:
        Player_rect.y -= speed_player
        Axe_rect.y -= speed_player
        for close in closers_gardens:
            if Player_rect.colliderect(close):
                Player_rect.y += speed_player
                break
    if down_move:
        Player_rect.y += speed_player
        Axe_rect.y += speed_player
        for close in closers_gardens:
            if Player_rect.colliderect(close):
                Player_rect.y -= speed_player
                break
    if right_move:
        Player_rect.x += speed_player
        Axe_rect.x += speed_player
        for close in closers_gardens:
            if Player_rect.colliderect(close):
                Player_rect.x -= speed_player
                break
    if left_move:
        Player_rect.x -= speed_player
        Axe_rect.x -= speed_player
        for close in closers_gardens:
            if Player_rect.colliderect(close):
                Player_rect.x += speed_player
                break

#Level
add_xp_level = 0
xp_level = 0.0
level = 0
max_level = 100
level_bar = 0.0

#Coins
coins = 50

coins_image = pygame.transform.scale(pygame.image.load("Image/Coins.png"), (50, 50))
coins_rect = coins_image.get_rect()
coins_rect.x = WIDTH-150
coins_rect.y = 10

#items
items = {"apple": {"id": 1, "name":"Apple", "image":"Image/Appal.png", "cost": 50}, "wood":{"id": 2, "name": "Wood", "image": "", "cost": 100}}
tools = {"axe": {"id": 1, "name": "Axe", "image": "Image/Axe.png", "cost": 50}}
UI_items = {"apple": {"id": 1, "name":"Apple", "image": pygame.transform.scale(pygame.image.load("Image/Appel.png"), (70, 70)), "cost": 50}, "wood":{"id": 2, "name": "Wood", "image": pygame.transform.scale(pygame.image.load("Image/Wood.png"), (70, 70)), "cost": 100}}

#Item Appel
apel_in_screen = True
aple_count = 0

Aple_image = pygame.transform.scale(pygame.image.load(items["apple"]["image"]), (20, 20))
Aple_rect = Aple_image.get_rect()
Aple_rect.x = 500
Aple_rect.y = 200

#Item Wood
wood_count = 0


#tools Axe
Axe_active = False
Axe_bay = False

Axe_image = pygame.transform.scale(pygame.image.load(tools["axe"]["image"]), (35, 30))
Axe_rect = Axe_image.get_rect()
Axe_rect.x = Player_rect.x + 40
Axe_rect.y = Player_rect.y + 10

#Pick Up Items
def Pick_Up_Items():
    global aple_count, apel_in_screen
    if Player_rect.colliderect(Aple_rect):
        if apel_in_screen:
            apel_in_screen = False
            aple_count += randint(1, 2)
            screen.blit(Aple_image, Aple_rect)

#UI Inventory
UI_Inventory_image = pygame.transform.scale(pygame.image.load("Image/UI_Inventory.png"), (750, 500))
UI_Inventory_rect = UI_Inventory_image.get_rect()
UI_Inventory_rect.x = 100
UI_Inventory_rect.y = 100

#UI Inventory slot
UI_Inventory_slot_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (80, 80))
UI_Inventory_slot_rect = UI_Inventory_slot_image.get_rect()
UI_Inventory_slot_rect.x = UI_Inventory_rect.x + 20
UI_Inventory_slot_rect.y = UI_Inventory_rect.y + 50

#UI Inventory slot image
UI_Inventory_slot_item_image = UI_items["apple"]["image"]
UI_Inventory_slot_item_rect = UI_Inventory_slot_item_image.get_rect()
UI_Inventory_slot_item_rect.x = UI_Inventory_slot_rect.x + 5
UI_Inventory_slot_item_rect.y = UI_Inventory_slot_rect.y + 5

#UI Inventory text name 
name_slot = font1.render(items["apple"]["name"], True, WHITE)

#UI Inventory slot (1)
UI_Inventory_slot_image1 = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (80, 80))
UI_Inventory_slot_rect1 = UI_Inventory_slot_image1.get_rect()
UI_Inventory_slot_rect1.x = UI_Inventory_rect.x + 20
UI_Inventory_slot_rect1.y = UI_Inventory_rect.y + 150

#UI Inventory slot image(1)
UI_Inventory_slot_item_image1 = UI_items["wood"]["image"]
UI_Inventory_slot_item_rect1 = UI_Inventory_slot_item_image1.get_rect()
UI_Inventory_slot_item_rect1.x = UI_Inventory_slot_rect1.x + 5
UI_Inventory_slot_item_rect1.y = UI_Inventory_slot_rect1.y + 5

#UI Inventory text name(1)
name_slot1 = font1.render(items["wood"]["name"], True, WHITE)

#UI Inventory Level
UI_LevelBarBackgraund_image = pygame.transform.scale(pygame.image.load("Image/UI_BacgraundLevel.png"), (200, 30))
UI_LevelBarBackgraund_rect = UI_LevelBarBackgraund_image.get_rect()
UI_LevelBarBackgraund_rect.x = UI_Inventory_rect.x + 10
UI_LevelBarBackgraund_rect.y = UI_Inventory_rect.y + 430

#Inventory
Inventoty_active = False

def InventaryActive():
    global aple_count,Inventoty_active, text_count
    if Inventoty_active:
        screen.blit(UI_Inventory_image, UI_Inventory_rect)

        #Render Slot inventory N0
        screen.blit(UI_Inventory_slot_image, UI_Inventory_slot_rect)
        screen.blit(UI_Inventory_slot_item_image, UI_Inventory_slot_item_rect)
        screen.blit(name_slot, (UI_Inventory_slot_rect.x + 15, UI_Inventory_slot_rect.y + 75))
        
        #UI Inventory count apple ()
        text_count = str(aple_count)
        count_slot = font1.render(text_count, True, WHITE)
        screen.blit(count_slot, (UI_Inventory_slot_rect.x + 65, UI_Inventory_slot_rect.y + 50))

        #Render Slot inventory N1 
        screen.blit(UI_Inventory_slot_image1, UI_Inventory_slot_rect1)
        screen.blit(UI_Inventory_slot_item_image1, UI_Inventory_slot_item_rect1)
        screen.blit(name_slot1, (UI_Inventory_slot_rect1.x + 15, UI_Inventory_slot_rect1.y + 75))
        
        #UI Inventory count wood
        text_count1 = str(wood_count)
        count_slot1 = font1.render(text_count1, True, WHITE)
        screen.blit(count_slot1, (UI_Inventory_slot_rect1.x + 65, UI_Inventory_slot_rect1.y + 50))

        screen.blit(UI_LevelBarBackgraund_image, UI_LevelBarBackgraund_rect)
        screen.blit(UI_LevelBarBackgraund_image, UI_LevelBarBackgraund_rect)

        UI_level_bar_image = pygame.transform.scale(pygame.image.load("Image/UI_LevelBar.png"), (level_bar * 2, 30))
        UI_level_bar_rect = UI_level_bar_image.get_rect()
        UI_level_bar_rect.x = UI_LevelBarBackgraund_rect.x
        UI_level_bar_rect.y = UI_LevelBarBackgraund_rect.y
        screen.blit(UI_level_bar_image, UI_level_bar_rect)
        
        #UI Inventory Level Player
        text_Level = font1.render(f"Lvl:{level}", True, WHITE)
        screen.blit(text_Level, (UI_level_bar_rect.x + 80, UI_level_bar_rect.y + 5))

#UI Market 
UI_Market_image = pygame.transform.scale(pygame.image.load("Image/UI_inventory.png"), (750, 500))
UI_Market_rect = UI_Market_image.get_rect()
UI_Market_rect.x = 100
UI_Market_rect.y = 100

#UI Market slot
UI_Market_slot_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (70,70))
UI_Market_slot_rect = UI_Market_slot_image.get_rect()
UI_Market_slot_rect.x = UI_Market_rect.x + 20
UI_Market_slot_rect.y = UI_Market_rect.y + 20

#UI Market slot item
UI_Market_slot_item_image = pygame.transform.scale(pygame.image.load("Image/Axe.png"), (50,50))
UI_Market_slot_item_rect = UI_Market_slot_item_image.get_rect()
UI_Market_slot_item_rect.x = UI_Market_slot_rect.x + 5
UI_Market_slot_item_rect.y = UI_Market_slot_rect.y + 5

#UI Market button
UI_Market_button_image = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png"), (70, 20))
UI_Market_button_rect = UI_Market_button_image.get_rect()
UI_Market_button_rect.x = UI_Market_slot_rect.x
UI_Market_button_rect.y = UI_Market_slot_rect.y + 75

#UI Market text cost Axe
cost_Axe = str(tools["axe"]["cost"])
cost_item = font1.render(cost_Axe, True, WHITE)

#UI Market slot (1)
UI_Market_slot_image1 = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (70,70))
UI_Market_slot_rect1 = UI_Market_slot_image1.get_rect()
UI_Market_slot_rect1.x = UI_Market_rect.x + 20
UI_Market_slot_rect1.y = UI_Market_rect.y + 130

#UI Market slot item (1)
UI_Market_slot_item_image1 = pygame.transform.scale(pygame.image.load("Image/Appel.png"), (50,50))
UI_Market_slot_item_rect1 = UI_Market_slot_item_image1.get_rect()
UI_Market_slot_item_rect1.x = UI_Market_slot_rect1.x + 5
UI_Market_slot_item_rect1.y = UI_Market_slot_rect1.y + 5

#UI Market button (1)
UI_Market_button_image1 = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png"), (70, 20))
UI_Market_button_rect1 = UI_Market_button_image1.get_rect()
UI_Market_button_rect1.x = UI_Market_slot_rect1.x
UI_Market_button_rect1.y = UI_Market_slot_rect1.y + 75

#UI Market text cost (1)
cost_item1 = font1.render(str(items["apple"]["cost"]), True, WHITE)

#UI Market slot (2)
UI_Market_slot_image2 = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (70,70))
UI_Market_slot_rect2 = UI_Market_slot_image2.get_rect()
UI_Market_slot_rect2.x = UI_Market_rect.x + 20
UI_Market_slot_rect2.y = UI_Market_rect.y + 230

#UI Market slot item (2)
UI_Market_slot_item_image2 = pygame.transform.scale(pygame.image.load("Image/Wood.png"), (50,50))
UI_Market_slot_item_rect2 = UI_Market_slot_item_image2.get_rect()
UI_Market_slot_item_rect2.x = UI_Market_slot_rect2.x + 5
UI_Market_slot_item_rect2.y = UI_Market_slot_rect2.y + 5

#UI Market button (2)
UI_Market_button_image2 = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png"), (70, 20))
UI_Market_button_rect2 = UI_Market_button_image2.get_rect()
UI_Market_button_rect2.x = UI_Market_slot_rect2.x
UI_Market_button_rect2.y = UI_Market_slot_rect2.y + 75

#UI Market text cost (2)
cost_item2 = font1.render(str(items["wood"]["cost"]), True, WHITE)

#UI Market slotG
UI_Market_slotG_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (60,60))
UI_Market_slotG_rect = UI_Market_slotG_image.get_rect()
UI_Market_slotG_rect.x = UI_Market_rect.x + 100
UI_Market_slotG_rect.y = UI_Market_rect.y + 20

#UI Market slotG item
UI_Market_slotG_item_image = pygame.transform.scale(pygame.image.load("Image/garden.png"), (50,50))
UI_Market_slotG_item_rect = UI_Market_slotG_item_image.get_rect()
UI_Market_slotG_item_rect.x = UI_Market_slotG_rect.x + 3
UI_Market_slotG_item_rect.y = UI_Market_slotG_rect.y + 3

#UI Market slotG Backgraund text
UI_Market_backgraund_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (150,60))
UI_Market_backgraund_rect  = UI_Market_backgraund_image.get_rect()
UI_Market_backgraund_rect.x = UI_Market_slotG_rect.x + 70
UI_Market_backgraund_rect.y = UI_Market_slotG_rect.y 

#UI Market slotG button
UI_Market__button_image = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png"), (60, 60))
UI_Market__button_rect = UI_Market_button_image.get_rect()
UI_Market__button_rect.x = UI_Market_slotG_rect.x + 200
UI_Market__button_rect.y = UI_Market_slotG_rect.y 

UI_Market_text_garden = font1.render("Need: 2Lvl and 100coins", True, WHITE)

#Market Objact
Market_image = pygame.transform.scale(pygame.image.load("Image/Market.png"),(150, 120))
Market_rect = Market_image.get_rect()
Market_rect.x = 200
Market_rect.y = 10



#Market
Market_active = False
Market_Items = False
Market_Garden =False 
def Market():
    if  Market_active:
        #UI Market slot Axe
        screen.blit(UI_Market_image, UI_Market_rect)
        screen.blit(UI_Market_slot_image, UI_Market_slot_rect)
        screen.blit(UI_Market_slot_item_image, UI_Market_slot_item_rect)
        screen.blit(UI_Market_button_image, UI_Market_button_rect)

        #UI Market cost Axe
        screen.blit(cost_item, (UI_Market_slot_rect.x + 55, UI_Market_slot_rect.y + 50))
            
        #UI Market slot Apple
        screen.blit(UI_Market_slot_image1, UI_Market_slot_rect1)
        screen.blit(UI_Market_slot_item_image1, UI_Market_slot_item_rect1)
        screen.blit(UI_Market_button_image1, UI_Market_button_rect1)

        #UI Market cost Aplle
        screen.blit(cost_item1, (UI_Market_slot_rect1.x + 55, UI_Market_slot_rect1.y + 50))

        #UI Market slot Wood
        screen.blit(UI_Market_slot_image2, UI_Market_slot_rect2)
        screen.blit(UI_Market_slot_item_image2, UI_Market_slot_item_rect2)
        screen.blit(UI_Market_button_image2, UI_Market_button_rect2)

        #UI Market cost Wood
        screen.blit(cost_item2, (UI_Market_slot_rect2.x + 55, UI_Market_slot_rect2.y + 50))

        #UI Market garden
        screen.blit(UI_Market_slotG_image, UI_Market_slotG_rect)
        screen.blit(UI_Market_slotG_item_image, UI_Market_slotG_item_rect)
        screen.blit(UI_Market__button_image, UI_Market__button_rect)
        screen.blit(UI_Market_backgraund_image, UI_Market_backgraund_rect)
        screen.blit(UI_Market_text_garden, (UI_backgraund_rect.x + 5, UI_backgraund_rect.y + 5))
        
    


#UI Orders
UI_Orders_image = pygame.transform.scale(pygame.image.load("Image/UI_Inventory.png"), (720, 500))
UI_Orders_rect = UI_Orders_image.get_rect()
UI_Orders_rect.x = 100
UI_Orders_rect.y = 100

#UI Order slot
UI_Orders_slot_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (80,80))
UI_Orders_slot_rect = UI_Orders_image.get_rect()
UI_Orders_slot_rect.x = UI_Orders_rect.x + 20
UI_Orders_slot_rect.y = UI_Orders_rect.y + 50

#UI Order slot item
UI_Orders_slot_item_image = UI_items["apple"]["image"]
UI_Orders_slot_item_rect = UI_Orders_slot_item_image.get_rect()
UI_Orders_slot_item_rect.x = UI_Orders_slot_rect.x + 5
UI_Orders_slot_item_rect.y = UI_Orders_slot_rect.y + 5

#UI Order Backgraund text
UI_backgraund_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (300,80))
UI_backgraund_rect  = UI_backgraund_image.get_rect()
UI_backgraund_rect.x = UI_Orders_slot_rect.x + 100
UI_backgraund_rect.y = UI_Orders_slot_rect.y 

#UI Orders button
UI_Orders_button_image = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png"), (70, 20))
UI_Orders_button_rect = UI_Orders_button_image.get_rect()
UI_Orders_button_rect.x = UI_Orders_slot_rect.x + 400
UI_Orders_button_rect.y = UI_Orders_slot_rect.y  

#UI Order slot (1)
UI_Orders_slot_image1 = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (80,80))
UI_Orders_slot_rect1 = UI_Orders_image.get_rect()
UI_Orders_slot_rect1.x = UI_Orders_rect.x + 20
UI_Orders_slot_rect1.y = UI_Orders_rect.y + 150

#UI Order slot item (1)
UI_Orders_slot_item_image1 = UI_items["wood"]["image"]
UI_Orders_slot_item_rect1 = UI_Orders_slot_item_image1.get_rect()
UI_Orders_slot_item_rect1.x = UI_Orders_slot_rect1.x + 5
UI_Orders_slot_item_rect1.y = UI_Orders_slot_rect1.y + 5

#UI Order Backgraund text (1)
UI_backgraund_image1 = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (300,80))
UI_backgraund_rect1  = UI_backgraund_image1.get_rect()
UI_backgraund_rect1.x = UI_Orders_slot_rect1.x + 100
UI_backgraund_rect1.y = UI_Orders_slot_rect1.y 

#UI Orders button (1)
UI_Orders_button_image1 = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png"), (70, 20))
UI_Orders_button_rect1 = UI_Orders_button_image1.get_rect()
UI_Orders_button_rect1.x = UI_Orders_slot_rect1.x + 400
UI_Orders_button_rect1.y = UI_Orders_slot_rect1.y 

#Order
Order_active = False

#Order Objact
Order_image = pygame.transform.scale(pygame.image.load("Image/Border_order.png"),(110, 100))
Order_rect = Order_image.get_rect()
Order_rect.x = 10
Order_rect.y = 10

#Order Progres
Order_complect = False
Order_complect1 = False

list_orders = {"0":{"image": pygame.transform.scale(pygame.image.load("Image/Appel.png"), (70, 70)), "pay": 20, "count_need": 15},"1":{"image": pygame.transform.scale(pygame.image.load("Image/Appel.png"), (70, 70)), "pay": 60, "count_need": 50},
               "2":{"image": pygame.transform.scale(pygame.image.load("Image/Wood.png"), (70, 70)), "pay": 50, "count_need": 20},"3":{"image": pygame.transform.scale(pygame.image.load("Image/Wood.png"), (70, 70)), "pay": 100, "count_need": 60}}

#Chenge Orders
num_items_list = 0
count_items_need = 0
num_items_list1 = 0
count_items_need1 = 0
def Change_Order():
    global num_items_list, UI_Orders_slot_item_image, count_items_need, Order_complect, UI_Order_text
    if Order_complect == False:
        num_items_list = randint(0, 1)
        UI_Orders_slot_item_image =  list_orders[f"{num_items_list}"]["image"]
        count_items_need = list_orders[f"{num_items_list}"]["count_need"]
        #UI Order text
        font = pygame.font.Font(None, 28)
        pay = list_orders[f"{num_items_list}"]["pay"]
        text_order = f"Собери {count_items_need}: Награда {pay}"
        UI_Order_text = font.render(text_order, True, WHITE)
        Order_complect = True
    

def Change_Order1():
    global num_items_list1, UI_Orders_slot_item_image1, count_items_need1, Order_complect1, UI_Order_text1
    if Order_complect1 == False:
        num_items_list1 = randint(2, 3)
        UI_Orders_slot_item_image1 =  list_orders[f"{num_items_list1}"]["image"]
        count_items_need1 = list_orders[f"{num_items_list1}"]["count_need"]
        #UI Order text
        font = pygame.font.Font(None, 28)
        pay = list_orders[f"{num_items_list1}"]["pay"]
        text_order1 = f"Собери {count_items_need}: Награда {pay}"
        UI_Order_text1 = font.render(text_order1, True, WHITE)
        Order_complect1 = True
     

def Orders():
    if Order_active:
        #Order Appel 
        screen.blit(UI_Orders_image, UI_Orders_rect)
        screen.blit(UI_Orders_slot_image, UI_Orders_slot_rect)
        screen.blit(UI_Orders_slot_item_image, UI_Orders_slot_item_rect)
        screen.blit(UI_Orders_button_image, UI_Orders_button_rect)
        screen.blit(UI_backgraund_image, UI_backgraund_rect)
        screen.blit(UI_Order_text, (UI_backgraund_rect.x + 5, UI_backgraund_rect.y + 5))
        
        #Order  Wood
        screen.blit(UI_Orders_slot_image1, UI_Orders_slot_rect1)
        screen.blit(UI_Orders_slot_item_image1, UI_Orders_slot_item_rect1)
        screen.blit(UI_Orders_button_image1, UI_Orders_button_rect1)
        screen.blit(UI_backgraund_image1, UI_backgraund_rect1)
        screen.blit(UI_Order_text1, (UI_backgraund_rect1.x + 5, UI_backgraund_rect1.y + 5))
         
        
    

#Garden
garden_active = True
grow = False
timer = 0
Apple_true = False
def garden():
    global timer, Garden_rect, FinishTree_image, FinishTree_rect, Apple_true

    Garden_image = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
    Garden_rect = Garden_image.get_rect()
    Garden_rect.x = WIDTH-250
    Garden_rect.y = HEIGHT-500

    sead_image =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
    sead_rect = sead_image.get_rect()
    sead_rect.x = Garden_rect.x + 5
    sead_rect.y = Garden_rect.y + 5

    StartTree_image = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
    StartTree_rect =StartTree_image.get_rect()
    StartTree_rect.x = Garden_rect.x + 5
    StartTree_rect.y = Garden_rect.y - 30

    FinishTree_image =pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
    FinishTree_rect = FinishTree_image.get_rect()
    FinishTree_rect.x = Garden_rect.x + 5
    FinishTree_rect.y = Garden_rect.y - 40

    ApelTree_image =pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
    ApelTree_rect = ApelTree_image.get_rect()
    ApelTree_rect.x = Garden_rect.x + 5
    ApelTree_rect.y = Garden_rect.y - 40

    screen.blit(Garden_image, Garden_rect)
    timer += 1/60

    if grow and garden_active:
        if timer >=0 and timer <= 5:
            screen.blit(sead_image, sead_rect)
        if timer >= 5 and timer <= 10:
            screen.blit(StartTree_image, StartTree_rect)

        if timer >= 10 and timer <= 15:
            screen.blit(FinishTree_image, FinishTree_rect)
        if timer >= 15:
            screen.blit(ApelTree_image, ApelTree_rect)

#Garden1
garden_active1 = True
grow1 = False
timer1 = 0

def garden1():
    global timer1, Garden_rect1, FinishTree_image1, FinishTree_rect1

    Garden_image1 = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
    Garden_rect1 = Garden_image1.get_rect()
    Garden_rect1.x = 120
    Garden_rect1.y = HEIGHT-620

    sead_image1 =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
    sead_rect1 = sead_image1.get_rect()
    sead_rect1.x = Garden_rect1.x + 5
    sead_rect1.y = Garden_rect1.y + 5

    StartTree_image1 = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
    StartTree_rect1 =StartTree_image1.get_rect()
    StartTree_rect1.x = Garden_rect1.x + 5
    StartTree_rect1.y = Garden_rect1.y - 30

    FinishTree_image1 =pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
    FinishTree_rect1 = FinishTree_image1.get_rect()
    FinishTree_rect1.x = Garden_rect1.x + 5
    FinishTree_rect1.y = Garden_rect1.y - 40

    ApelTree_image1 =pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
    ApelTree_rect1 = ApelTree_image1.get_rect()
    ApelTree_rect1.x = Garden_rect1.x + 5
    ApelTree_rect1.y = Garden_rect1.y - 40

    screen.blit(Garden_image1, Garden_rect1)
    timer1 += 1/60

    if grow1 and garden_active1:
        if timer1 >=0 and timer1 <= 5:
            screen.blit(sead_image1, sead_rect1)
        if timer1 >= 5 and timer1 <= 10:
            screen.blit(StartTree_image1, StartTree_rect1)

        if timer1 >= 10 and timer1 <= 15:
            screen.blit(FinishTree_image1, FinishTree_rect1)
        if timer1 >= 15:
            screen.blit(ApelTree_image1, ApelTree_rect1)

#Garden2
garden_active2 = False
grow2 = False
timer2 = 0

def garden2():
    global timer2, Garden_rect2, FinishTree_image2, FinishTree_rect2, close_rect2

    Garden_image2 = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
    Garden_rect2 = Garden_image2.get_rect()
    Garden_rect2.x = 330
    Garden_rect2.y = HEIGHT-620

    sead_image2 =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
    sead_rect2 = sead_image2.get_rect()
    sead_rect2.x = Garden_rect2.x + 5
    sead_rect2.y = Garden_rect2.y + 5

    StartTree_image2 = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
    StartTree_rect2 =StartTree_image2.get_rect()
    StartTree_rect2.x = Garden_rect2.x + 5
    StartTree_rect2.y = Garden_rect2.y - 30

    FinishTree_image2 =pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
    FinishTree_rect2 = FinishTree_image1.get_rect()
    FinishTree_rect2.x = Garden_rect2.x + 5
    FinishTree_rect2.y = Garden_rect2.y - 40

    ApelTree_image2 =pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
    ApelTree_rect2 = ApelTree_image2.get_rect()
    ApelTree_rect2.x = Garden_rect2.x + 5
    ApelTree_rect2.y = Garden_rect2.y - 40

    screen.blit(Garden_image2, Garden_rect2)
    timer2 += 1/60

    if grow2 and garden_active2:
        if timer2 >=0 and timer2 <= 5:
            screen.blit(sead_image2, sead_rect2)
        if timer >= 5 and timer2 <= 10:
            screen.blit(StartTree_image2, StartTree_rect2)

        if timer2 >= 10 and timer2 <= 15:
            screen.blit(FinishTree_image2, FinishTree_rect2)
        if timer2 >= 15:
            screen.blit(ApelTree_image2, ApelTree_rect2)

    if garden_active2 == False:
        close_image2 = pygame.transform.scale(pygame.image.load("Image/image.png"), (120, 120))
        close_rect2 = close_image2.get_rect()
        close_rect2.x = 300
        close_rect2.y = HEIGHT-640
        screen.blit(close_image2,close_rect2)
    
    closers_gardens.append(close_rect2)

#Garden3
garden_active3 = False
grow3 = False
timer3 = 0
def garden3():
    global timer3, Garden_rect3, FinishTree_image3, FinishTree_rect3

    Garden_image3 = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
    Garden_rect3 = Garden_image3.get_rect()
    Garden_rect3.x = 540
    Garden_rect3.y = HEIGHT-620

    sead_image3 =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
    sead_rect3 = sead_image3.get_rect()
    sead_rect3.x = Garden_rect3.x + 5
    sead_rect3.y = Garden_rect3.y + 5

    StartTree_image3 = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
    StartTree_rect3 =StartTree_image3.get_rect()
    StartTree_rect3.x = Garden_rect3.x + 5
    StartTree_rect3.y = Garden_rect3.y - 30

    FinishTree_image3 =pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
    FinishTree_rect3 = FinishTree_image3.get_rect()
    FinishTree_rect3.x = Garden_rect3.x + 5
    FinishTree_rect3.y = Garden_rect3.y - 40

    ApelTree_image3 =pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
    ApelTree_rect3 = ApelTree_image3.get_rect()
    ApelTree_rect3.x = Garden_rect3.x + 5
    ApelTree_rect3.y = Garden_rect3.y - 40

    screen.blit(Garden_image3, Garden_rect3)
    timer3 += 1/60

    if grow3 and garden_active3:
        if timer3 >=0 and timer3 <= 5:
            screen.blit(sead_image3, sead_rect3)
        if timer3 >= 5 and timer3 <= 10:
            screen.blit(StartTree_image3, StartTree_rect3)

        if timer3 >= 10 and timer3 <= 15:
            screen.blit(FinishTree_image3, FinishTree_rect3)
        if timer3 >= 15:
            screen.blit(ApelTree_image3, ApelTree_rect3)
    
    if garden_active3 == False:
        close_image3 = pygame.transform.scale(pygame.image.load("Image/image.png"), (120, 120))
        close_rect3 = close_image3.get_rect()
        close_rect3.x = 510
        close_rect3.y = HEIGHT-640
        screen.blit(close_image3,close_rect3)
    
    closers_gardens.append(close_rect3)

#Garden4
garden_active4 = False
grow4 = False
timer4 = 0

def garden4():
    global timer4, Garden_rect4, FinishTree_image4, FinishTree_rect4

    Garden_image4 = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
    Garden_rect4 = Garden_image4.get_rect()
    Garden_rect4.x = 760
    Garden_rect4.y = HEIGHT-620

    sead_image4 =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
    sead_rect4 = sead_image4.get_rect()
    sead_rect4.x = Garden_rect4.x + 5
    sead_rect4.y = Garden_rect4.y + 5

    StartTree_image4 = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
    StartTree_rect4 =StartTree_image4.get_rect()
    StartTree_rect4.x = Garden_rect4.x + 5
    StartTree_rect4.y = Garden_rect4.y - 30

    FinishTree_image4 =pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
    FinishTree_rect4 = FinishTree_image4.get_rect()
    FinishTree_rect4.x = Garden_rect4.x + 5
    FinishTree_rect4.y = Garden_rect4.y - 40

    ApelTree_image4 =pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
    ApelTree_rect4 = ApelTree_image4.get_rect()
    ApelTree_rect4.x = Garden_rect4.x + 5
    ApelTree_rect4.y = Garden_rect4.y - 40

    screen.blit(Garden_image4, Garden_rect4)
    timer4 += 1/60

    if grow4 and garden_active4:
        if timer4 >=0 and timer4 <= 5:
            screen.blit(sead_image4, sead_rect4)
        if timer4 >= 5 and timer4 <= 10:
            screen.blit(StartTree_image4, StartTree_rect4)

        if timer4 >= 10 and timer4 <= 15:
            screen.blit(FinishTree_image, FinishTree_rect)
        if timer4 >= 15:
            screen.blit(ApelTree_image4, ApelTree_rect4)
    
    if garden_active4 == False:
        close_image4 = pygame.transform.scale(pygame.image.load("Image/image.png"), (120, 120))
        close_rect4 = close_image4.get_rect()
        close_rect4.x = 720
        close_rect4.y = HEIGHT-640
        screen.blit(close_image4,close_rect4)

    closers_gardens.append(close_rect4)

#Garden5
garden_active5 = False
grow5 = False
timer5 = 0

def garden5():
    global timer5, Garden_rect5, FinishTree_image5, FinishTree_rect5

    Garden_image5 = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
    Garden_rect5 = Garden_image5.get_rect()
    Garden_rect5.x = 120
    Garden_rect5.y = HEIGHT-350

    sead_image5 =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
    sead_rect5 = sead_image5.get_rect()
    sead_rect5.x = Garden_rect5.x + 5
    sead_rect5.y = Garden_rect5.y + 5

    StartTree_image5 = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
    StartTree_rect5 =StartTree_image5.get_rect()
    StartTree_rect5.x = Garden_rect5.x + 5
    StartTree_rect5.y = Garden_rect5.y - 30

    FinishTree_image5 =pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
    FinishTree_rect5 = FinishTree_image5.get_rect()
    FinishTree_rect5.x = Garden_rect5.x + 5
    FinishTree_rect5.y = Garden_rect5.y - 40

    ApelTree_image5 =pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
    ApelTree_rect5 = ApelTree_image5.get_rect()
    ApelTree_rect5.x = Garden_rect5.x + 5
    ApelTree_rect5.y = Garden_rect5.y - 40

    screen.blit(Garden_image5, Garden_rect5)
    timer5 += 1/60

    if grow5 and garden_active5:
        if timer5 >=0 and timer5 <= 5:
            screen.blit(sead_image5, sead_rect5)
        if timer5 >= 5 and timer5 <= 10:
            screen.blit(StartTree_image5, StartTree_rect5)

        if timer5 >= 10 and timer5 <= 15:
            screen.blit(FinishTree_image5, FinishTree_rect5)
        if timer5 >= 15:
            screen.blit(ApelTree_image5, ApelTree_rect5)
    
    if garden_active5 == False:
        close_image5 = pygame.transform.scale(pygame.image.load("Image/image.png"), (120, 120))
        close_rect5 = close_image5.get_rect()
        close_rect5.x = 90
        close_rect5.y = HEIGHT-370
        screen.blit(close_image5,close_rect5)
    
    closers_gardens.append(close_rect5)

#Garden6
garden_active6 = False
grow6 = False
timer6 = 0

def garden6():
    global timer6, Garden_rect6, FinishTree_image6, FinishTree_rect6

    Garden_image6 = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
    Garden_rect6 = Garden_image6.get_rect()
    Garden_rect6.x = 330
    Garden_rect6.y = HEIGHT-350

    sead_image6 =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
    sead_rect6 = sead_image6.get_rect()
    sead_rect6.x = Garden_rect6.x + 5
    sead_rect6.y = Garden_rect6.y + 5

    StartTree_image6 = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
    StartTree_rect6 =StartTree_image6.get_rect()
    StartTree_rect6.x = Garden_rect6.x + 5
    StartTree_rect6.y = Garden_rect6.y - 30

    FinishTree_image6 =pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
    FinishTree_rect6 = FinishTree_image6.get_rect()
    FinishTree_rect6.x = Garden_rect6.x + 5
    FinishTree_rect6.y = Garden_rect6.y - 40

    ApelTree_image6 =pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
    ApelTree_rect6 = ApelTree_image6.get_rect()
    ApelTree_rect6.x = Garden_rect6.x + 5
    ApelTree_rect6.y = Garden_rect6.y - 40

    screen.blit(Garden_image6, Garden_rect6)
    timer6 += 1/60

    if grow6 and garden_active6:
        if timer6 >=0 and timer6 <= 5:
            screen.blit(sead_image6, sead_rect6)
        if timer6 >= 5 and timer6 <= 10:
            screen.blit(StartTree_image6, StartTree_rect6)

        if timer6 >= 10 and timer6 <= 15:
            screen.blit(FinishTree_image6, FinishTree_rect6)
        if timer6 >= 15:
            screen.blit(ApelTree_image6, ApelTree_rect6)

    
    if garden_active6 == False:
        close_image6 = pygame.transform.scale(pygame.image.load("Image/image.png"), (120, 120))
        close_rect6 = close_image6.get_rect()
        close_rect6.x = 300
        close_rect6.y = HEIGHT-370
        screen.blit(close_image6,close_rect6)
    
    closers_gardens.append(close_rect6)

#Garden7
garden_active7 = False
grow7 = False
timer7 = 0

def garden7():
    global timer7, Garden_rect7, FinishTree_image7, FinishTree_rect7

    Garden_image7 = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
    Garden_rect7 = Garden_image7.get_rect()
    Garden_rect7.x = 540
    Garden_rect7.y = HEIGHT-350

    sead_image7 =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
    sead_rect7 = sead_image7.get_rect()
    sead_rect7.x = Garden_rect7.x + 5
    sead_rect7.y = Garden_rect7.y + 5

    StartTree_image7 = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
    StartTree_rect7 =StartTree_image7.get_rect()
    StartTree_rect7.x = Garden_rect7.x + 5
    StartTree_rect7.y = Garden_rect7.y - 30

    FinishTree_image7 =pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
    FinishTree_rect7 = FinishTree_image7.get_rect()
    FinishTree_rect7.x = Garden_rect7.x + 5
    FinishTree_rect7.y = Garden_rect7.y - 40

    ApelTree_image7 =pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
    ApelTree_rect7 = ApelTree_image7.get_rect()
    ApelTree_rect7.x = Garden_rect7.x + 5
    ApelTree_rect7.y = Garden_rect7.y - 40

    screen.blit(Garden_image7, Garden_rect7)
    timer7 += 1/60


    if grow7 and garden_active7:
        if timer7 >=0 and timer7 <= 5:
            screen.blit(sead_image7, sead_rect7)
        if timer7 >= 5 and timer7 <= 10:
            screen.blit(StartTree_image7, StartTree_rect7)

        if timer7 >= 10 and timer7 <= 15:
            screen.blit(FinishTree_image, FinishTree_rect)
        if timer7 >= 15:
            screen.blit(ApelTree_image7, ApelTree_rect7)

    if garden_active7 == False:
        close_image7 = pygame.transform.scale(pygame.image.load("Image/image.png"), (120, 120))
        close_rect7 = close_image7.get_rect()
        close_rect7.x = 510
        close_rect7.y = HEIGHT-370
        screen.blit(close_image7,close_rect7)

    closers_gardens.append(close_rect7)


#Garden8
garden_active8 = False
grow8 = False
timer8 = 0

def garden8():
    global timer8, Garden_rect8, FinishTree_image8, FinishTree_rect8

    Garden_image8 = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
    Garden_rect8 = Garden_image8.get_rect()
    Garden_rect8.x = 760
    Garden_rect8.y = HEIGHT-350

    sead_image8 =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
    sead_rect8 = sead_image8.get_rect()
    sead_rect8.x = Garden_rect8.x + 5
    sead_rect8.y = Garden_rect8.y + 5

    StartTree_image8 = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
    StartTree_rect8 =StartTree_image8.get_rect()
    StartTree_rect8.x = Garden_rect8.x + 5
    StartTree_rect8.y = Garden_rect8.y - 30

    FinishTree_image8 =pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
    FinishTree_rect8 = FinishTree_image8.get_rect()
    FinishTree_rect8.x = Garden_rect8.x + 5
    FinishTree_rect8.y = Garden_rect8.y - 40

    ApelTree_image8 =pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
    ApelTree_rect8 = ApelTree_image8.get_rect()
    ApelTree_rect8.x = Garden_rect8.x + 5
    ApelTree_rect8.y = Garden_rect8.y - 40

    screen.blit(Garden_image8, Garden_rect8)
    timer8 += 1/60

    if grow8 and garden_active8:
        if timer8 >=0 and timer8 <= 5:
            screen.blit(sead_image8, sead_rect8)
        if timer8 >= 5 and timer8 <= 10:
            screen.blit(StartTree_image8, StartTree_rect8)

        if timer8 >= 10 and timer8 <= 15:
            screen.blit(FinishTree_image8, FinishTree_rect8)
        if timer8 >= 15:
            screen.blit(ApelTree_image8, ApelTree_rect8)
    if garden_active8 == False:
        close_image8 = pygame.transform.scale(pygame.image.load("Image/image.png"), (120, 120))
        close_rect8 = close_image8.get_rect()
        close_rect8.x = 720
        close_rect8.y = HEIGHT-370
    
    closers_gardens.append(close_rect8)

#Garden9
garden_active9 = False
grow = False
timer = 0
def garden():
    global timer, Garden_rect, FinishTree_image, FinishTree_rect, Apple_true

    Garden_image = pygame.transform.scale(pygame.image.load("Image/garden.png"), (60, 60))
    Garden_rect = Garden_image.get_rect()
    Garden_rect.x = WIDTH-250
    Garden_rect.y = HEIGHT-500

    sead_image =pygame.transform.scale(pygame.image.load("Image/sead.png"), (50, 50))
    sead_rect = sead_image.get_rect()
    sead_rect.x = Garden_rect.x + 5
    sead_rect.y = Garden_rect.y + 5

    StartTree_image = pygame.transform.scale(pygame.image.load("Image/Start_tree.png"),(40, 90))
    StartTree_rect =StartTree_image.get_rect()
    StartTree_rect.x = Garden_rect.x + 5
    StartTree_rect.y = Garden_rect.y - 30

    FinishTree_image =pygame.transform.scale(pygame.image.load("Image/FinishTree.png"), (60, 95))
    FinishTree_rect = FinishTree_image.get_rect()
    FinishTree_rect.x = Garden_rect.x + 5
    FinishTree_rect.y = Garden_rect.y - 40

    ApelTree_image =pygame.transform.scale(pygame.image.load("Image/TreewithApel.png"), (60, 95))
    ApelTree_rect = ApelTree_image.get_rect()
    ApelTree_rect.x = Garden_rect.x + 5
    ApelTree_rect.y = Garden_rect.y - 40

    screen.blit(Garden_image, Garden_rect)
    timer += 1/60
# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up_move = True
            if event.key == pygame.K_s:
                down_move = True
            if event.key == pygame.K_d:
                right_move = True
            if event.key == pygame.K_a:
                left_move = True
            if event.key == pygame.K_i:
                if Market_active == False and Inventoty_active == False and Order_active == False:
                    Inventoty_active = True
                else:
                    Inventoty_active = False
            if event.key == pygame.K_1:
                if Axe_bay:
                    if Axe_active == False:
                        Axe_active =True
                    else:
                        Axe_active = False
                print(Axe_active, Axe_bay)
            if event.key == pygame.K_e:
                if Market_active == False and Inventoty_active == False and Order_active == False and Player_rect.colliderect(Market_rect):
                    Market_active = True
                    Market_Items = True
                else:
                    Market_active = False
                    Market_Items = False
                if Order_active == False and Market_active == False and Inventoty_active == False and Player_rect.colliderect(Order_rect):
                    Order_active = True
                else:
                    Order_active = False
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up_move = False
            if event.key == pygame.K_s:
                down_move = False
            if event.key == pygame.K_d:
                right_move = False
            if event.key == pygame.K_a:
                left_move = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and Player_rect.colliderect(Garden_rect1) and grow1 == False and aple_count >= 1:
                aple_count -= 1
                grow1 = True
                timer1 = 0

            if event.button == 1 and Player_rect.colliderect(Garden_rect2) and grow2 == False and aple_count >= 1 and garden_active2:
                aple_count -= 1
                grow2 = True
                timer2 = 0

            if event.button == 1 and Player_rect.colliderect(Garden_rect3) and grow3 == False and aple_count >= 1 and garden_active3:
                aple_count -= 1
                grow3 = True
                timer3 = 0
            
            if event.button == 1 and Player_rect.colliderect(Garden_rect4) and grow4 == False and aple_count >= 1 and garden_active4:
                aple_count -= 1
                grow4 = True
                timer4 = 0

            if event.button == 1 and Player_rect.colliderect(Garden_rect5) and grow5 == False and aple_count >= 1 and garden_active5:
                aple_count -= 1
                grow5 = True
                timer5 = 0

            if event.button == 1 and Player_rect.colliderect(Garden_rect6) and grow6 == False and aple_count >= 1 and garden_active6:
                aple_count -= 1
                grow6 = True
                timer6 = 0

            if event.button == 1 and Player_rect.colliderect(Garden_rect7) and grow7 == False and aple_count >= 1 and garden_active7:
                aple_count -= 1
                grow7 = True
                timer7 = 0

            if event.button == 1 and Player_rect.colliderect(Garden_rect8) and grow8 == False and aple_count >= 1 and garden_active8:
                aple_count -= 1
                grow8 = True
                timer8 = 0

            #grow1
            if event.button == 1 and Player_rect.colliderect(Garden_rect1) and grow1 == True and timer1 >= 15 and Axe_active:
                add_xp_level = randint(1000, 1500)
                xp_level += add_xp_level
                level_bar = xp_level/max_level
                aple_count += randint(10, 20)
                wood_count += 5
                grow1 = False
            #grow2
            if event.button == 1 and Player_rect.colliderect(Garden_rect2) and grow2 == True and timer2 >= 15 and Axe_active:
                add_xp_level = randint(1000, 1500)
                xp_level += add_xp_level
                level_bar = xp_level/max_level
                aple_count += randint(10, 20)
                wood_count += 5
                grow2 = False
            #grow3
            if event.button == 1 and Player_rect.colliderect(Garden_rect3) and grow3 == True and timer3 >= 15 and Axe_active:
                add_xp_level = randint(1000, 1500)
                xp_level += add_xp_level
                level_bar = xp_level/max_level
                aple_count += randint(10, 20)
                wood_count += 5
                grow3 = False
            #grow4
            if event.button == 1 and Player_rect.colliderect(Garden_rect4) and grow4 == True and timer4 >= 15 and Axe_active:
                add_xp_level = randint(1000, 1500)
                xp_level += add_xp_level
                level_bar = xp_level/max_level
                aple_count += randint(10, 20)
                wood_count += 5
                grow4 = False
            #grow5
            if event.button == 1 and Player_rect.colliderect(Garden_rect5) and grow5 == True and timer5 >= 15 and Axe_active:
                add_xp_level = randint(1000, 1500)
                xp_level += add_xp_level
                level_bar = xp_level/max_level
                aple_count += randint(10, 20)
                wood_count += 5
                grow5 = False
            #grow6
            if event.button == 1 and Player_rect.colliderect(Garden_rect6) and grow6 == True and timer6 >= 15 and Axe_active:
                add_xp_level = randint(1000, 1500)
                xp_level += add_xp_level
                level_bar = xp_level/max_level
                aple_count += randint(10, 20)
                wood_count += 5
                grow6 = False
            #grow7
            if event.button == 1 and Player_rect.colliderect(Garden_rect7) and grow7 == True and timer7 >= 15 and Axe_active:
                add_xp_level = randint(1000, 1500)
                xp_level += add_xp_level
                level_bar = xp_level/max_level
                aple_count += randint(10, 20)
                wood_count += 5
                grow7 = False
            #grow8
            if event.button == 1 and Player_rect.colliderect(Garden_rect8) and grow8 == True and timer8 >= 15 and Axe_active:
                add_xp_level = randint(1000, 1500)
                xp_level += add_xp_level
                level_bar = xp_level/max_level
                aple_count += randint(10, 20)
                wood_count += 5
                grow8 = False
            
            if event.button == 1 and UI_Market_button_rect.collidepoint(event.pos) and coins >= tools["axe"]["cost"]:
                if Axe_bay == False:
                    coins -= tools["axe"]["cost"]
                    Axe_bay = True
                    
            if event.button == 1 and UI_Market_button_rect1.collidepoint(event.pos) and coins >= str(items["apple"]["cost"]):
                coins -= items["apple"]["cost"]
                aple_count += 1
            
            if event.button == 1 and UI_Market_button_rect1.collidepoint(event.pos) and coins >= str(items["wood"]["cost"]):
                coins -= items["wood"]["cost"]
                aple_count += 1
                
                
                    
            if event.button == 1 and UI_Orders_button_rect.collidepoint(event.pos) and Order_complect and aple_count >= list_orders[f"{num_items_list}"]["count_need"]:
                Order_complect = False
            if event.button == 1 and UI_Orders_button_rect1.collidepoint(event.pos) and Order_complect1 and wood_count >= list_orders[f"{num_items_list1}"]["count_need"]:
                Order_complect = False

    screen.fill(BLACK)
    #check LevelBar full
    if level_bar >= 100:
        xp_level -= 100
        level += 1
        level_bar = xp_level/max_level
    bacgraund()
    moving_player()
    Pick_Up_Items()
    if apel_in_screen:
        screen.blit(Aple_image, Aple_rect)

    garden1()
    garden2()
    garden3()
    garden4()
    garden5()
    garden6()
    garden7()
    garden8()
    

    screen.blit(Order_image, Order_rect)
    screen.blit(Market_image, Market_rect)

    screen.blit(Player_image, Player_rect)
    if Axe_active:
        screen.blit(Axe_image, Axe_rect)

    #Coins render
    screen.blit(coins_image, coins_rect)
    coins_text = font.render(f"{coins}", True, WHITE)
    screen.blit(coins_text, (coins_rect.x + 60, 15))
    
    Market()
    InventaryActive()
    Orders()
    Change_Order()
    Change_Order1()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
