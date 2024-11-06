import pygame
pygame.init()
#
display = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
#
scene = [
    "XXXXXXXXXXXXXXXXXXXXXX",
    "X--------------------X",
    "X--------------------X",
    "X--------------------X",
    "XXXXXXXX-------------X",
    "X--------------------X",
    "X------X-------------X",
    "X--XX--XXXXXXXXXXXXXXX",
    "X--XX--X-------------X",
    "X--------------------X",
    "X------X-------------X",
    "XXXXXXXXXXXXXXXXXXXXXX"]
#
mappa = pygame.Surface((len(scene[0])*64,len(scene)*64)) 
x,y = 0,0
for row in scene:
    for tile in row:
        if tile in "-":
            pygame.draw.rect(mappa,(0,155,0),((x,y),(64,64)))
        elif tile in "X":
            pygame.draw.rect(mappa,(125,125,125),((x,y),(64,64)))
        else:
            pygame.draw.rect(mappa,(255,128,122),((x,y),(64,64)))
        x += 64
    y += 64
    x = 0
#
class Player:
    def __init__(self):
        self.image = pygame.Surface((32,32))
        self.image.fill((255,0,0))
        self.rect = pygame.Rect((284,284),(32,32))
        self.map_pos = (0,0)
        self.moveBox = (100,100,500,500)
    def move(self):
        mx,my = self.map_pos
        key = pygame.key.get_pressed()
        if player.rect.x <= self.moveBox[0]:
            self.rect.x += 8
            mx += 8
        elif player.rect.x >= self.moveBox[2]-32:
            self.rect.x -= 8
            mx -= 8
        if player.rect.y <= self.moveBox[1]:
            self.rect.y += 8
            my += 8
        elif player.rect.y >= self.moveBox[3]-32:
            self.rect.y -= 8
            my -= 8
        self.map_pos = (mx,my)
    def render(self,display):
        display.blit(self.image,(self.rect.x,self.rect.y))
#
player = Player()
#
RUNNING = True
while RUNNING:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    #
    player.move()
    #
    display.fill((0,155,0))
    display.blit(mappa,player.map_pos)
    player.render(display)
    #
    pygame.display.flip()
#
pygame.quit()
