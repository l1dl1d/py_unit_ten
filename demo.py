# These two lines should be at the top of all Pygame programs
import pygame, sys
from pygame.locals import *




# Standard starting while loop for Pygame programs.
# Much more can be added to this as needed.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
