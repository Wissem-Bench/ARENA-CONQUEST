import pygame
import os
# from handler import Handler

class GameObject :

    def __init__(self, handler):
        self.handler = handler
        self.image = pygame.image.load(os.path.join('Assets', 'Idle.png'))   
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def tick(self):
        self.rect.x += 1
        self.rect.y += 1

    def draw(self):
        self.handler.game.WIN.blit(self.image ,self.rect)
        