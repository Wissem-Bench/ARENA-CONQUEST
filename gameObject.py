import pygame
import random
# import os
# from handler import Handler

class GameObject(pygame.sprite.Sprite) :
    
    def __init__(self, handler):
        super().__init__()
        self.handler = handler


        # self.image = pygame.Surface((120, 120))
        # self.image.set_colorkey((1, 2, 3))
        # self.image.fill((1, 2, 3))
        # pygame.draw.circle(self.image, pygame.Color(color), (60, 60), 60)
        # self.rect = self.image.get_rect(center=pos)
        
        

        # # self.image = pygame.image.load(os.path.join('Assets', 'Idle.png'))   
        # # self.rect = self.image.get_rect()
        # # self.rect.x = 0
        # # self.rect.y = 0

    # def check_color_collision(self, player, object):
    #     collision = False
    #     object = self.handler.game.gameState.objects
    #     for sprite in object :
    #         sprite.mask = pygame.mask.from_threshold(sprite.image, pygame.Color(self.handler.game.gameState.colors[0]), (1, 1, 1, 255))
    #         # print(self.handler.game.gameState.colors[1])
    #     if pygame.sprite.spritecollideany(player, object, pygame.sprite.collide_mask):
    #         collision = True
    #     return collision



    def tick(self):
        pass


    def draw(self):
        pass
        # # self.handler.game.WIN.blit(self.image ,self.rect)
        # # pygame.draw.circle(self.handler.game.WIN,(255,165,0),(910,910),self.cicleRadius,0)
        # # pygame.draw.circle(self.image, (240, 100, 0), self.center, 60)
        # self.handler.game.gameState.sprites.draw(self.handler.game.WIN)