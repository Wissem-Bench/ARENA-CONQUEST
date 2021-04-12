from ssTiles import SsTiles
from tiles import *
from player import Player
from enemy import Enemy
from handler import Handler
import pygame
import sys
from assets import Assets
from character import Character
pygame.init()

class Game:

    def __init__(self):
        pygame.display.set_caption("My Game")
        self.FPS = 60
        self.WIDTH = 900
        self.HEIGHT = 500
        self.WIN = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.dest = (100, 100)
        self.handler = Handler(self) 
        # should be before any other object that have handler in its const.
        # Handler(self) current instance in the current class
        self.assets = Assets()
        self.heroKnight = Character(self.handler,self.assets.heroknight,100,100,10,5)
        self.player = Player(self.handler, self.heroKnight)
        self.pressed = {
            "right key" : False,
            "left key" : False,
            "up key" : False,
            "down key" : False,
            "d key" : False
        }
        self.ssTile = SsTiles('spritesheet.png')
        self.map = TileMap('test_level.csv', self.ssTile)
        self.handler.init()

    def draw_window(self):
        self.WIN.fill(self.BLACK)
        # draw everything here:
        self.map.draw_map(self.WIN)
        self.heroKnight.draw()
        # self.enemy.draw()
        self.handler.characterManager.draw()

        # end of drawing
        pygame.display.flip()
        

    def tick(self):
        self.heroKnight.tick()
        self.player.tick()
        self.handler.characterManager.tick()


    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.FPS)
            self.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    print('game closed')
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    self.pressed[event.key] = False
            self.draw_window()