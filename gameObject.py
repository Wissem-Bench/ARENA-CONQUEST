import pygame
from assets import Assets
from spriteSheet import SpriteSheet
from animation import Animation
import random
# import os
# from handler import Handler

class GameObject(pygame.sprite.Sprite) :
    def __init__(self, handler, img, x, y): #,img
        super().__init__()
        self.handler = handler
        self.handler = handler
        self.image = pygame.image.load(f"Assets/{img}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_stairs_collision(self):
        for Character in self.handler.characterManager.characterGroup:
            collision = pygame.sprite.spritecollide(Character, self.handler.game.gameState.stairGroup, False, pygame.sprite.collide_mask)
            if len(collision) > 0:
                # print("collided")
                return True
            else:
                # print("not collided")
                return False

    def tick(self):
        # self.currentAnimation.tick()
        self.check_stairs_collision()


    def draw(self):
        self.handler.game.WIN.blit(self.image, (self.rect.x - self.handler.game.gameState.current_world.camera.xOffset,self.rect.y - self.handler.game.gameState.current_world.camera.yOffset))

# class GameObject(pygame.sprite.Sprite) :

    
#     def __init__(self, handler):
#         super().__init__()
#         self.handler = handler

#     def init(self):
#         self.test = pygame.sprite.Sprite
#         self.minotaur = pygame.image.load("Assets/Minotaur.png") #.convert()
#         self.rect_1 = [self.handler.game.WIN, (111, 210, 46), [250,100,100,100]]
#         # self.handler.init()
#         # self.assets = self.handler.game.assets
#         # self.assets.initAssets()
#         # self.tower_animation = [Animation(self.handler.game.assets.tower[0], 0.07), 
#         #                         Animation(self.handler.game.assets.tower[1], 0.07)]
#         # self.tower_health = 100
#         # self.currentAnimation = self.tower_animation[0]
#         # self.rect = self.currentAnimation.frames[0].get_rect()
#         # self.rect.x = 45
#         # self.rect.y = 45
#         # self.position = (self.rect.x, self.rect.y)


#     # def tower(self):
#     #     if self.tower_health == 0 :
#     #         self.currentAnimation = self.tower_animation[1]
#     #     return self.currentAnimation

#     # def tower_health(self):
#     #     if 
    

#         # self.image = pygame.Surface((120, 120))
#         # self.image.set_colorkey((1, 2, 3))
#         # self.image.fill((1, 2, 3))
#         # pygame.draw.circle(self.image, pygame.Color(color), (60, 60), 60)
#         # self.rect = self.image.get_rect(center=pos)
        
    

#         # # self.image = pygame.image.load(os.path.join('Assets', 'Idle.png'))   
#         # # self.rect = self.image.get_rect()
#         # # self.rect.x = 0
#         # # self.rect.y = 0

#     # def check_color_collision(self, player, object):
#     #     collision = False
#     #     object = self.handler.game.gameState.objects
#     #     for sprite in object :
#     #         sprite.mask = pygame.mask.from_threshold(sprite.image, pygame.Color(self.handler.game.gameState.colors[0]), (1, 1, 1, 255))
#     #         # print(self.handler.game.gameState.colors[1])
#     #     if pygame.sprite.spritecollideany(player, object, pygame.sprite.collide_mask):
#     #         collision = True
#     #     return collision



#     def tick(self):
#         # self.currentAnimation.tick()
#         self.init()


#     def draw(self):
#         self.handler.game.WIN.blit(self.kharya, (500 - self.handler.game.gameState.current_world.camera.xOffset,120))
#         # pygame.draw.rect(self.rect_1[0], self.rect_1[1],self.rect_1[2])
#         # self.init()
#         # self.handler.game.WIN.blit(self.currentAnimation.getCurrentFrame(),
#         # (self.rect.x - self.handler.game.gameState.current_world.camera.xOffset,
#         # self.rect.y - self.handler.game.gameState.current_world.camera.yOffset))
#         # # x_camera_offset = self.handler.game.gameState.current_world.camera.xOffset
#         # # y_camera_offset = self.handler.game.gameState.current_world.camera.yOffset
#         # # self.handler.game.WIN.blit(self.currentAnimation.getCurrentFrame(), (self.position[0] - x_camera_offset , self.position - y_camera_offset))
        
#         # # # self.handler.game.WIN.blit(self.image ,self.rect)
#         # # # pygame.draw.circle(self.handler.game.WIN,(255,165,0),(910,910),self.cicleRadius,0)
#         # # # pygame.draw.circle(self.image, (240, 100, 0), self.center, 60)
#         # # self.handler.game.gameState.sprites.draw(self.handler.game.WIN)