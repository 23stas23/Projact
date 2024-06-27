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
    bacgraund_image = pygame.transform.scale(pygame.image.load("Image/Backgraund.png"), (WIDTH, HEIGHT))
    bacgraund_rect = bacgraund_image.get_rect()
    bacgraund_rect.x = 0
    bacgraund_rect.y = 0
    screen.blit(bacgraund_image, bacgraund_rect)

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
    if down_move:
        Player_rect.y += speed_player
        Axe_rect.y += speed_player
    if right_move:
        Player_rect.x += speed_player
        Axe_rect.x += speed_player
    if left_move:
        Player_rect.x -= speed_player
        Axe_rect.x -= speed_player

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
tools = {"axe": {"id": 1, "name": "Axe", "image": "Image/Axe.png", "cost": 200}}
UI_items = {"apple": {"id": 1, "name":"Apple", "image": pygame.transform.scale(pygame.image.load("Image/Appal.png"), (70, 70)), "cost": 50}, "wood":{"id": 2, "name": "Wood", "image": pygame.transform.scale(pygame.image.load("Image/Appal.png"), "cost": 100}}

#Item
apel_in_screen = True
aple_count = 0

Aple_image = pygame.transform.scale(pygame.image.load(items["apple"]["image"]), (20, 20))
Aple_rect = Aple_image.get_rect()
Aple_rect.x = 500
Aple_rect.y = 200

#tools
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
UI_Inventory_slot_item_image = UI_item["apple"]["image"]
UI_Inventory_slot_item_rect = UI_Inventory_slot_item_image.get_rect()
UI_Inventory_slot_item_rect.x = UI_Inventory_slot_rect.x + 5
UI_Inventory_slot_item_rect.y = UI_Inventory_slot_rect.y + 5

#UI Inventory text name
name_slot = font1.render(items["apple"]["name"], True, WHITE)

#UI Inventory Level
UI_LevelBarBackgraund_image = pygame.transform.scale(pygame.image.load("Image/UI_BacgraundLevel.png"), (200, 30))
UI_LevelBarBackgraund_rect = UI_LevelBarBackgraund_image.get_rect()
UI_LevelBarBackgraund_rect.x = UI_Inventory_rect.x + 10
UI_LevelBarBackgraund_rect.y = UI_Inventory_rect.y + 430

#Inventory
Inventoty_active = False

def InventaryActive():
    global aple_count,Inventoty_active
    if Inventoty_active:
        screen.blit(UI_Inventory_image, UI_Inventory_rect)
        screen.blit(UI_Inventory_slot_image, UI_Inventory_slot_rect)
        screen.blit(UI_Inventory_slot_item_image, UI_Inventory_slot_item_rect)
        screen.blit(UI_LevelBarBackgraund_image, UI_LevelBarBackgraund_rect)
        UI_level_bar_image = pygame.transform.scale(pygame.image.load("Image/UI_LevelBar.png"), (level_bar * 2, 30))

        UI_level_bar_rect = UI_level_bar_image.get_rect()
        UI_level_bar_rect.x = UI_LevelBarBackgraund_rect.x
        UI_level_bar_rect.y = UI_LevelBarBackgraund_rect.y
        screen.blit(UI_level_bar_image, UI_level_bar_rect)
        screen.blit(name_slot, (UI_Inventory_slot_rect.x + 15, UI_Inventory_slot_rect.y + 75))
        #UI Inventory count item
        text_count = str(aple_count)
        count_slot = font1.render(text_count, True, WHITE)
        screen.blit(count_slot, (UI_Inventory_slot_rect.x + 65, UI_Inventory_slot_rect.y + 50))
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

#Market Objact
Market_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"),(100, 120))
Market_rect = Market_image.get_rect()
Market_rect.x = 200
Market_rect.y = 10

#Market
Market_active = False 
def Market():
    screen.blit(Market_image, Market_rect)
    if  Market_active:
        screen.blit(UI_Market_image, UI_Market_rect)
        screen.blit(UI_Market_slot_image, UI_Market_slot_rect)
        screen.blit(UI_Market_button_image, UI_Market_button_rect)
        screen.blit(UI_Market_slot_item_image, UI_Market_slot_item_rect)


#UI Orders
UI_Orders_image = pygame.transform.scale(pygame.image.load("Image/UI_Inventory.png"), (720, 500))
UI_Orders_rect = UI_Orders_image.get_rect()
UI_Orders_rect.x = 500
UI_Orders_rect.y = 400

#UI Order slot
UI_Orders_slot_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (50,50))
UI_Orders_slot_rect = UI_Orders_image.get_rect()
UI_Orders_slot_rect.x = UI_Orders_rect.x + 50
UI_Orders_slot_rect.y = UI_Orders_rect.y + 100

#UI Order slot item
UI_Orders_slot_item_image = pygame.transform.scale(pygame.image.load("Image/UI_slot_inventory.png"), (40,40))
UI_Orders_slot_item_rect = UI_Orders_slot_item_image.get_rect()
UI_Orders_slot_item_rect.x = UI_Orders_slot_rect.x + 5
UI_Orders_slot_item_rect.y = UI_Orders_slot_rect.y + 5

#UI Orders button
UI_Orders_button_image = pygame.transform.scale(pygame.image.load("Image/UI_button_Market.png"), (70, 20))
UI_Orders_button_rect = UI_Orders_button_image.get_rect()
UI_Orders_button_rect.x = UI_Orders_slot_rect.x
UI_Orders_button_rect.y = UI_Orders_slot_rect.y + 75

#Order
Order_active = False

#Order Objact
Order_image = pygame.transfor.scale(pygame.image.load("Image/UI_slot_inventory.png"),(100, 120))
Order_rect = Order_image.get_rect()
Order_rect.x = 10
Order_rect.y = 10

def Orders():
    screen.blit(Order_image, Order_rect)
    if Order_active:
        screen.blit(UI_Orders_image, UI_Orders_rect)
        screen.blit(UI_Orders_slot_image, UI_Orders_slot_rect)
        screen.blit(UI_Orders_slot_item_image, UI_Orders_slot_item_rect)
        screen.blit(UI_Orders_button_image, UI_Orders_button_rect)

#Order Progres
Order_complect = False

list_orders = {"0":{"image": pygame.transform.scale(pygame.image.load("Image/Appal.png"), (70, 70)), "pay": 20, "count_need": 15},"1":{"image": pygame.transform.scale(pygame.image.load("Image/Appal.png"), (70, 70)), "pay": 60, "count_need": 50}}

#Chenge Orders
num_items_list = 0
count_items_need = 0
timer_order = 0.0
def Change_Order():
    global num_items_list, UI_Orders_slot_item_image, timer_order
    timer_order = 1/FPS/60
    timer_order = round(timer_order, 2)
    print(timer_order)
    if Order_complect == False:
        timer_order = 0.0
        if timer_order == 2.0
        num_item_list = randint(0, 1)
        UI_Orders_slot_item_image =  list_orders[f"num_items_list"]["image"]
        count_items_need = list_orders[f"num_items_list"]["count_need"]
        
        
        
    

#Garden
grow = False
timer = 0
def garden():
    global timer, Garden_rect

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

    if grow:
        if timer >=0 and timer <= 5:
            screen.blit(sead_image, sead_rect)
        if timer >= 5 and timer <= 10:
            screen.blit(StartTree_image, StartTree_rect)

        if timer >= 10 and timer <= 15:
            screen.blit(FinishTree_image, FinishTree_rect)
        if timer >= 15:
            screen.blit(ApelTree_image, ApelTree_rect)


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
                if Market_active == False and Inventoty_active == False and Order_active == False and Player.colliderect(Market_rect):
                    Market_active = True
                else:
                    Market_active = False
                if Order_active == False and Market_active == False and Inventoty_active == False and Player.colliderect(Order_rect):
                    Order_active = True
                else:
                    Order_active = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and Player_rect.colliderect(Garden_rect) and grow == False and aple_count >= 1:
                aple_count -= 1
                grow = True
                timer = 0
            if event.button == 1 and Player_rect.colliderect(Garden_rect) and grow == True and timer >= 3 and Axe_active:
                add_xp_level = randint(1000, 1500)
                xp_level += add_xp_level
                level_bar = xp_level/max_level
                aple_count += randint(10, 20)
                grow = False
            if event.button == 1 and UI_Orders_button_rect.collidepoint(event.pos) and Order_complect:
                Order_complect = False
            
            if event.button == 1 and UI_Market_button_rect.collidepoint(event.pos) and coins >= 50:
                if Axe_bay == False:
                    coins -= 50
                    Axe_bay = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up_move = False
            if event.key == pygame.K_s:
                down_move = False
            if event.key == pygame.K_d:
                right_move = False
            if event.key == pygame.K_a:
                left_move = False

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
    garden()
    screen.blit(Player_image, Player_rect)
    if Axe_active:
        screen.blit(Axe_image, Axe_rect)

    #Coins render
    screen.blit(coins_image, coins_rect)
    coins_text = font.render(f"{coins}", True, WHITE)
    screen.blit(coins_text, (coins_rect.x + 60, 15))
    
    Market()
    InventaryActive()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
