import pygame
from enemyController import EnemyController
from enemiesList import Skeleton

class EnemyManager():

    def __init__(self, handler):
        self.handler = handler
        self.enemyGroup = pygame.sprite.Group()
        skeleton = Skeleton(self.handler)
        self.enemy = EnemyController(self.handler, skeleton)
        self.enemy_spawn(self.enemy.character, 250, 250)

    def enemy_spawn(self, character, x, y):
        # self.enemy = enemy(self.handler, self.handler.game.assets.skeleton, x, y)
        character.rect.x = x
        character.rect.y = y
        self.enemyGroup.add(character)

    def tick(self):
        # for enemy in self.enemyGroup:
        #     enemy.tick()
        self.enemy.tick()
    
    def draw(self):
        # for enemy in self.enemyGroup:
        #     enemy.draw()
        self.enemy.draw()