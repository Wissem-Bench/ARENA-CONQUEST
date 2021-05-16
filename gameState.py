import pygame
# from gameCamera import GameCamera
from player import Player
from gameObject import GameObject
from world import World
import random
from enemiesList import Skeleton
from enemyController import EnemyController
from heroesList import *

class GameState():

    def __init__(self, handler):
        self.handler = handler
        
    def init(self):
        self.handler.init()
        # self.enemies_controller_list = []
        self.world_1 = World(self.handler, "battle_arena.png") #, "battle_arena.png"
        self.world_1.init()
        self.current_world = self.world_1
        self.player = Player(self.handler)

        self.skeleton = Skeleton(self.handler)
        self.evil = EvilWizard(self.handler)
        self.ronin = Ronin(self.handler)
        self.skeleton.controller = EnemyController(self.handler, self.skeleton)
        self.ronin.controller = EnemyController(self.handler, self.ronin)
        self.evil.controller = EnemyController(self.handler, self.evil)
        self.handler.characterManager.enemy_spawn(self.skeleton, 600, 250, self.world_1)
        self.handler.characterManager.enemy_spawn(self.ronin, 2400, 250, self.world_1)
        self.handler.characterManager.enemy_spawn(self.evil, 500, 150, self.world_1)
        # self.ronin.moveLeft = True #in behave
        # self.evil.moveLeft = True
        
        # self.ronin_controller = EnemyController(self.handler, self.ronin)
        
        # to be deleted
        # self.enemies_controller_list.append(self.skeleton_controller)
        # self.enemies_controller_list.append(self.ronin_controller)
        # self.enemies_controller_list.append(self.evil_controller)
        # self.handler.characterManager.enemies.extend(self.enemies_controller_list)

        # self.worldswitcher = {
        #     "world_1" : True ,
        #     "world_2" : False ,
        #     "world_3" : False
        # }


    # def current_world(self): # both skeletons have SAME reference !??

        # self.world.world_creator([[self.skeleton, 200, 200], [self.skeleton, 300, 300]])
        # self.skeleton.moveRight = True

    def tick(self):
        self.current_world.tick() # include characterManager
        self.player.tick()
        # self.skeleton.tick()
        # if self.worldswitcher["world_1"] == True:
        #     self.world.world_1()
        # elif self.worldswitcher["world_2"] == True:
        #     self.world.world_2()
        # elif self.worldswitcher["world_3"] == True:
        #     self.world.world_3()
        
    def draw(self):
        # self.current_world()
        self.current_world.draw()
        self.player.draw()