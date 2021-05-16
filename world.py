import pygame
import pytmx
# from pytmx.util_pygame import load_pygame
import pyscroll

from handler import Handler
from enemiesList import *
from gameCamera import GameCamera

class World():
    
    def __init__(self, handler, background) :
        self.handler = handler
        self.background = background
        
    def init(self):
        # self.tmx_data = pytmx.load_pygame("background.tmx")
        # map_data = pyscroll.data.TiledMapData(self.tmx_data)
        # map_layer = pyscroll.BufferedRenderer(map_data, self.handler.game.WIN.get_size())
        # map_layer.zoom = 2
        # self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 1)
        self.bg = pygame.image.load(f"Assets/{self.background}").convert()
        self.bg = pygame.transform.scale(self.bg, (int(3836/1), int(656/1)))
        self.camera = GameCamera(self.handler)
        self.handler.characterManager.init()
        self.walls = []
        # self.playersGroup.add(self.handler.game.choosencharacter)
        # self.enemyGroup = pygame.sprite.Group()

    def map(self):
        for object in self.tmx_data.objects:
            if object.type == "collision":
                self.walls.append(pygame.Rect(object.x, object.y, object.width, object.height))

    def tick(self):
        self.handler.characterManager.tick()

    def draw(self):
        # self.group.center((self.camera.xOffset, self.camera.yOffset))
        # print("center: " + str(self.handler.game.gameState.player.hero.rect.center))
        # self.group.draw(self.handler.game.WIN)
        self.handler.game.WIN.blit(self.bg, (0 - self.camera.xOffset, 0 - self.camera.yOffset))
        self.handler.characterManager.draw()

    # def world_1(self):
    #     self.backgroun44d = pygame.image.load("Assets/world_1.png").convert()
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