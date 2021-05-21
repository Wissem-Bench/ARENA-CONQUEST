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
        self.stairGroup = pygame.sprite.Group()
        self.stair1 = GameObject(self.handler,'stairFL', 185,242)
        self.stair2 = GameObject(self.handler,'stairSL', 305,265)
        self.stair3 = GameObject(self.handler,'stairFR', 3570,245)
        self.stair4 = GameObject(self.handler,'stairSR', 3440,265)
        self.stairGroup.add(self.stair1, self.stair2, self.stair3, self.stair4)
        
        self.left_pillar = GameObject(self.handler,'left_pillar', 1120,0)
        self.right_pillar = GameObject(self.handler,'right_pillar', 2450,0)
        # self.gameObject.init()
        self.world_1 = World(self.handler, "battle_arena.png") #, "battle_arena.png"
        self.world_1.init()
        self.current_world = self.world_1
        self.player = Player(self.handler)
        # self.tower = self.assets.tower
        # self.skeleton = Skeleton(self.handler)
        # self.skeleton_2 = Skeleton(self.handler)
        # self.evil = EvilWizard(self.handler)
        # self.ronin = Ronin(self.handler)
        # self.heroknight = HeroKnight(self.handler)
        # self.tower = Tower(self.handler)
        # self.skeleton.controller = EnemyController(self.handler, self.skeleton)
        # self.skeleton_2.controller = EnemyController(self.handler, self.skeleton_2)
        # self.ronin.controller = EnemyController(self.handler, self.ronin)
        # self.evil.controller = EnemyController(self.handler, self.evil)
        # self.heroknight.controller = EnemyController(self.handler, self.heroknight)
        # self.tower.controller = EnemyController(self.handler, self.tower)
        # self.handler.characterManager.enemy_spawn(self.tower, 25, -20)
        # self.handler.characterManager.enemy_spawn(self.skeleton, 1000, 250)
        # self.handler.characterManager.enemy_spawn(self.ronin, 2400, 250)
        # self.handler.characterManager.enemy_spawn(self.heroknight, 500, 150)
        # self.handler.characterManager.enemy_spawn(self.evil, 1000, 250)
        # self.handler.characterManager.enemy_spawn(self.skeleton_2, 100, 250)


    # def cur_wor(self):
    #     if self.player.hero.dead == True :
    #         self.current_world = self.death_world #death_world(black_WIN, remove all char -hero)


    def tick(self):
        self.current_world.tick() # include characterManager
        self.player.tick()
        self.stair1.tick()
        self.stair2.tick()
        self.stair3.tick()
        self.stair4.tick()
        
    def draw(self):
        self.current_world.draw()
        self.stair1.draw()
        self.stair2.draw()
        self.stair3.draw()
        self.stair4.draw()
        self.player.draw()
        self.right_pillar.draw()
        self.left_pillar.draw()
        # self.rightbeam