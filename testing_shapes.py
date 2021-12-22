import pygame, sys
from pygame.locals import *

pygame.init()
mainsurface = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption("Some Shapes")
mainsurface.fill((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

