# from ssTiles import SsTiles
# from tiles import *
# from player import Player
# from enemy import Enemy
from handler import Handler
import pygame
import sys
from assets import Assets
# from character import Character
from gameCamera import GameCamera
from gameState import GameState
from menuState import MenuState
from heroesList import HeroKnight
pygame.init()

class Game:

    def __init__(self):
        pygame.display.set_caption("AREA CONQUEST")
        self.FPS = 60
        self.WIDTH = 900
        self.HEIGHT = 500
        self.WIN = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.dest = (100, 100)
        self.handler = Handler(self) 
        # should be before any other object that have handler in its constr.
        # Handler(self) current instance in the current class
        
        self.assets = Assets(self.handler)
        self.menuState = MenuState(self.handler)
        self.menuState.init()
        self.gameState = GameState(self.handler)
        self.gameState.init()
        self.currentState = self.menuState

        
        # draw everything here:
    def draw_window(self):
        self.WIN.fill(self.BLACK)
        self.currentState.draw()

        # end of drawing
        pygame.display.flip()
        

    def tick(self):
        self.currentState.tick()


    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.FPS)
            self.handler.inputManager.tick()
            self.tick()
            self.draw_window()