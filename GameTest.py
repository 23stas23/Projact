import pygame

class Game:
  # Инициализация Pygame
  pygame.init()

  # Настройка окна
  WIDTH = 1000
  HEIGHT = 500
  FPS = 60

  # Цвета
  BLACK = (0, 0, 0)
  
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  
  pygame.display.set_caption("Farm")
  
  clock = pygame.time.Clock()

  # Цвета
  BLACK = (0, 0, 0)

