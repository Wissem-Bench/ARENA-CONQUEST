import pygame
# from gameCamera import GameCamera
from player import Player
from gameObject import GameObject
from world import World
import random
from enemiesList import Skeleton

class GameState():

    def __init__(self, handler):
        self.handler = handler
        
    def init(self):
        self.handler.init()
        self.world = World(self.handler)
        self.world.init()
        self.assets = self.handler.game.assets
        self.assets.initGameAssets()
        # self.camera = GameCamera(self.handler)
        self.background = "battle_arena.png"
        self.player = Player(self.handler)
        self.skeleton = Skeleton(self.handler)
        # self.worldswitcher = {
        #     "world_1" : True ,
        #     "world_2" : False ,
        #     "world_3" : False
        # }


    def current_world(self):
        self.world.world_creator(self.background, [[self.skeleton, 200, 200], [self.skeleton, 300, 300]])
        self.skeleton.moveRight = True
    def tick(self):
        self.player.tick()
        # self.skeleton.tick()
        self.skeleton.tick()

        
        # if self.worldswitcher["world_1"] == True:
        #     self.world.world_1()
        # elif self.worldswitcher["world_2"] == True:
        #     self.world.world_2()
        # elif self.worldswitcher["world_3"] == True:
        #     self.world.world_3()
        
    def draw(self):
        self.current_world()
        self.player.draw()
        # self.colors = ['yellow']
        # self.sprites = pygame.sprite.Group()
        # self.objects = pygame.sprite.Group()
        
        # for _ in range(4):
        #     pos = random.randint(100, 400), random.randint(100, 400)
        #     self.circle = GameObject(self.handler, pos, random.choice(self.colors), self.sprites, self.objects)

    # def worlds(self):
    #     self.world.enemiesAppear(character, x, y)
    
        