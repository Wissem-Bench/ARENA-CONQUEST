import pygame
from gameCamera import GameCamera
from player import Player
# from enemy import Enemy
from gameObject import GameObject
import random

class GameState():

    def __init__(self, handler):
        self.handler = handler
        
    def init(self):
        self.handler.init()
        self.assets = self.handler.game.assets
        self.assets.initGameAssets()
        self.camera = GameCamera(self.handler)
        self.player = Player(self.handler)
        self.colors = ['green', 'yellow', 'white', 'blue']
        self.sprites = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        
        for _ in range(20):
            pos = random.randint(100, 700), random.randint(100, 600)
            self.circle = GameObject(self.handler, pos, random.choice(self.colors), self.sprites, self.objects)

    # def switchState(self, state):
    #   self.currentState = state
    #   if type(state) is GameState:
    #       self.handler.setUIManager(self.handler.game.gameState.gameUiManager)
    #   elif type(state) is MenuState:
    #       self.handler.setUIManager(self.handler.game.menuState.menuUiManager)

    
        
    def tick(self):
        self.player.tick()
        self.handler.characterManager.tick()
        # self.gameObject.tick()
        
    def draw(self):
        self.handler.game.WIN.blit(self.assets.bg, (0 - self.camera.xOffset, 0 - self.camera.yOffset))
        # self.handler.characterManager.draw()
        self.player.draw()
        self.circle.draw()