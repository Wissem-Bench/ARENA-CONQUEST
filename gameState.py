import pygame
# from gameCamera import GameCamera
from player import Player
from animation import Animation
# from gameObject import GameObject
from world import World
from enemiesList import *
from enemyController import EnemyController
from heroesList import *
from gameObject import GameObject

class GameState():

    def __init__(self, handler):
        self.handler = handler
        
    def init(self):
        self.handler.init()
        self.assets = self.handler.game.assets
        self.assets.initAssets()
        self.gameObject = GameObject(self.handler)
        self.gameObject.init()
        self.world_1 = World(self.handler, "battle_arena.png") #, "battle_arena.png"
        self.world_1.init()
        self.current_world = self.world_1
        self.player = Player(self.handler)
        # self.tower = self.assets.tower
        self.skeleton = Skeleton(self.handler)
        # self.skeleton_2 = Skeleton(self.handler)
        self.evil = EvilWizard(self.handler)
        self.ronin = Ronin(self.handler)
        self.heroknight = HeroKnight(self.handler)
        self.tower = Tower(self.handler)
        self.skeleton.controller = EnemyController(self.handler, self.skeleton)
        # # self.skeleton_2.controller = EnemyController(self.handler, self.skeleton_2)
        self.ronin.controller = EnemyController(self.handler, self.ronin)
        self.evil.controller = EnemyController(self.handler, self.evil)
        self.heroknight.controller = EnemyController(self.handler, self.heroknight)
        self.tower.controller = EnemyController(self.handler, self.tower)
        self.handler.characterManager.enemy_spawn(self.tower, 0, 0, self.world_1)
        self.handler.characterManager.enemy_spawn(self.skeleton, 600, 250, self.world_1)
        self.handler.characterManager.enemy_spawn(self.ronin, 2400, 250, self.world_1)
        self.handler.characterManager.enemy_spawn(self.heroknight, 500, 150, self.world_1)
        self.handler.characterManager.enemy_spawn(self.evil, 1000, 250, self.world_1)
        # self.handler.characterManager.enemy_spawn(self.skeleton_2, 100, 250, self.world_1)

        # self.worldswitcher = {
        #     "world_1" : True ,
        #     "world_2" : False ,
        #     "world_3" : False
        # }


    # def cur_wor(self):
    #     if self.player.hero.dead == True :
    #         self.current_world = self.death_world #death_world(black_WIN, remove all char -hero)


    def tick(self):
        self.current_world.tick() # include characterManager
        self.player.tick()
        self.gameObject.tick()

        # if self.worldswitcher["world_1"] == True:
        #     self.world.world_1()
        # elif self.worldswitcher["world_2"] == True:
        #     self.world.world_2()
        # elif self.worldswitcher["world_3"] == True:
        #     self.world.world_3()
        
    def draw(self):
        self.current_world.draw()
        self.player.draw()
        self.gameObject.draw()