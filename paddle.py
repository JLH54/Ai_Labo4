# This Python file uses the following encoding: utf-8
from actor import actor
import pygame

class paddle(actor):
    def __init__(self, x,y,width,height, speed):
        super().__init__(x,y,width,height, speed)
        self.playerRectangle = pygame.Rect(self.x,self.y, self.width, self.height)
        pass

    def get_paddle(self):
        return self.playerRectangle

    def render(self, screen):
         self.rect = pygame.draw.rect(screen, pygame.Color(255,255,255), self.playerRectangle)
