import pygame
import math
import random
import os

pygame.init()

display_width = 800
display_height = 600

blue = (3,169,244)
blue2 = (63,81,181)

small = (50, 50)
normal = (math.ceil(small[0] * 1.5), math.ceil(small[1] * 1.5))
medium = (math.ceil(normal[0] * 1.5), math.ceil(normal[1] * 1.5))
large = (math.ceil(medium[0] * 2.5), math.ceil(medium[1] * 2.5))

pink_flower_1 = pygame.image.load(os.path.join('assets', 'pink_flower.png'))
pink_flower_2 = pygame.image.load(os.path.join('assets', 'pink_flower_2.png'))
pink_flower_3 = pygame.image.load(os.path.join('assets', 'pink_flower_3.png'))

screen_size = (display_width, display_height)
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

def paint_flower(flower, x, y, width, height, rotation = 0):
  tr = pygame.transform.scale(flower, (width, height))
  tr = pygame.transform.rotate(tr, rotation)
  screen.blit(tr, (x, y))


def paint_small_flower(flower, x, y):
  paint_flower(flower, x, y, small[0], small[1])


def paint_normal_flower(flower, x, y):
  paint_flower(flower, x, y, normal[0], normal[1])


def paint_medium_flower(flower, x, y):
  paint_flower(flower, x, y, medium[0], medium[1])


def paint_large_flower(flower, x, y):
  paint_flower(flower, x, y, large[0], large[1])


def paint_random(flower):
  size = random.randint(100, 200)
  x = random.randint(0, 750)
  y = random.randint(0, 550)
  rot = random.randint(1, 360)
  paint_flower(flower, x, y, size, size, rot)


def paint_border(left_flower, top_flower, bottom_flower):
  # Top
  pygame.draw.rect(screen, blue2, (0, 0, 800, 50))
  # Bottom
  pygame.draw.rect(screen, blue2, (0, 550, 800, 600))
  # Left
  pygame.draw.rect(screen, blue2, (0, 0, 50, 600))
  # Right
  pygame.draw.rect(screen, blue2, (750, 0, 750, 600))

  for i in range(0, 800, 50):
    paint_small_flower(top_flower, i, 0)
    paint_small_flower(bottom_flower, i, 550)

  for i in range(50, 550, 50):
    paint_small_flower(left_flower, 0, i)


def paint():
  screen.fill(blue)

  paint_random(pink_flower_1)
  paint_random(pink_flower_2)
  paint_random(pink_flower_3)

  paint_large_flower(pink_flower_3, 60, 60)
  paint_normal_flower(pink_flower_1, 180, 100)
  paint_medium_flower(pink_flower_2, 220, 220)
  paint_small_flower(pink_flower_3, 500, 400)

  paint_border(pink_flower_1, pink_flower_2, pink_flower_3)

  pygame.display.update()
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

paint()
