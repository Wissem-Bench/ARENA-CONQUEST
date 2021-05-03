import pygame
from handler import Handler
from enemiesList import *
from gameCamera import GameCamera
from enemyManager import EnemyManager

class World():
    
    def __init__(self, handler, background) :
        self.handler = handler
        self.background = background
        
    def init(self):
        self.bg = pygame.image.load(f"Assets/{self.background}").convert()
        self.camera = GameCamera(self.handler)
        self.enemyManager = EnemyManager(self.handler)
        # self.playersGroup.add(self.handler.game.choosencharacter)
        # self.enemyGroup = pygame.sprite.Group()

    def tick(self):
        self.enemyManager.tick()

    def draw(self):
        self.handler.game.WIN.blit(self.bg, (0 - self.camera.xOffset, 0 - self.camera.yOffset))
        self.enemyManager.draw()

    # def world_1(self):
    #     self.background = pygame.image.load("Assets/world_1.png").convert()
    #     self.handler.game.WIN.blit(self.background, (0 - self.camera.xOffset, 0 - self.camera.yOffset))
    #     self.enemiesAppear(self.skeleton, 200, 200)

    # def world_2(self):
    #     self.background = pygame.image.load("Assets/world_1.png").convert()
    #     self.handler.game.WIN.blit(self.background, (0 - self.camera.xOffset, 0 - self.camera.yOffset))
    #     self.enemiesAppear(skeleton, 200, 200)

    # def world_3(self):
    #     self.background = pygame.image.load("Assets/world_1.png").convert()
    #     self.handler.game.WIN.blit(self.background, (0 - self.camera.xOffset, 0 - self.camera.yOffset))
    #     self.enemiesAppear(skeleton, 200, 200)