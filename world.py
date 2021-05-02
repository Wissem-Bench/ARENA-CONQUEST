import pygame
from handler import Handler
from enemiesList import *
from gameCamera import GameCamera

class World():
    
    def __init__(self, handler) :
        self.handler = handler
        self.assets = self.handler.game.assets
        self.assets.initGameAssets()
        self.enemyGroup = pygame.sprite.Group()
        # self.playersGroup = pygame.sprite.Group()
        
    def init(self):
        self.camera = GameCamera(self.handler)
        self.skeleton = Skeleton(self.handler)
        # self.playersGroup.add(self.handler.game.choosencharacter)
        # self.enemyGroup = pygame.sprite.Group()

    def enemiesAppear(self,character, x, y):
        self.enemyGroup.add(character)
        character.rect.x = x
        character.rect.y = y
        # character.rect.x += character.velocity
        # character.moveRight = True
        # character.move()
        character.tick()
        character.draw()
        # character.moveRight = True
        # character.move()
        # character.check_collision(self.handler.game.choosencharacter, self.enemyGroup)
        # character.check_collision(character, self.playersGroup)

    def world_creator(self, background, enemies) :
        bg = pygame.image.load(f"Assets/{background}").convert()
        # bg = pygame.transform.scale(bg, (int(1920*1.25), int(1080*1.25)))
        self.handler.game.WIN.blit(bg, (0 - self.camera.xOffset, 0 - self.camera.yOffset))
        for i in range(len(enemies)):
            self.enemiesAppear(enemies[i][0], enemies[i][1], enemies[i][2]) 
            # self.world.world_creator(self.background, [[self.skeleton, 200, 200], [self.skeleton, 300, 300]])
            # def enemiesAppear(self,character, x, y):
            #     self.enemyGroup.add(character)
            #     character.rect.x = x
            #     character.rect.y = y
            #     character.draw()
            #     character.tick()

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

        