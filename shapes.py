import pygame

class Shapes:

    def __init__(self, surface):
        self.mainsurface = surface

    def draw_rectangle(self):
        pygame.draw.rect(self.mainsurface, (267, 255, 200), (270, 5, 60, 60))

    def draw_circle(self, pos):
        pass # remove this when you start to write your method

    def draw_ellipse(self):
        pass # remove this when you start to write your method

    def draw_z(self):
        pass # remove this when you start to write your method

    def draw_pentagon(self):
       pass # remove this when you start to write your method