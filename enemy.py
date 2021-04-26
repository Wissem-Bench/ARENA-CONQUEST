import pygame
from animation import Animation
from character import Character
from player import Player

class Enemy(Character):

    def __init__(self, handler, asset, x, y):
        super().__init__(handler, asset, 30, 30, 5, 1)
        self.handler = handler

    def standard_move(self):
        if not self.handler.enemyManager.check_collision(self, self.handler.game.character.characterGroup):
            return self.moveLeft
    
    def tick(self):
        # self.animationManager()
        # self.currentAnimation.tick()
        # self.image = self.currentAnimation.getCurrentFrame()
        self.standard_move()

    def draw(self):
        self.handler.game.WIN.blit(self.currentAnimation.getCurrentFrame(), self.rect)