import pygame
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

