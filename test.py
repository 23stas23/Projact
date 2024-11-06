import pygame
import sys
import random
import subprocess


# _______initiate Game______________ #
class Game:
    pygame.init()
    width = 800
    height = 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Game")
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    white = [255, 255, 255]
    black = [0, 0, 0]
    lblue = [159, 210, 255]
    background = input(
        "What color background would you like? (White, Black, or Light Blue): ")
    if background == "White":
        screen.fill(white)
        pygame.display.flip()
    elif background == "Black":
        screen.fill(black)
        pygame.display.update()
    elif background == "Light Blue":
        screen.fill(lblue)
        pygame.display.update()
    else:
        screen.fill(black)
        pygame.display.update()
    for "." in "map1.txt":
        pygame.image.load("winter.Wall.png")



# ___________________TO RUN___________________________ #
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if event.type == pygame.KEYDOWN:
        command = "python JakeGame.py"
        subprocess.call(command)

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.type == pygame.K_ESCAPE:
            pygame.quit()
# _______________________________________________ #

pygame.quit()
