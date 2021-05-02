import pygame
from heroesList import *



class Player:

    def __init__(self,handler):
        self.handler = handler
        self.playersGroup = pygame.sprite.Group()
        self.hero = self.handler.game.choosenHero
        self.playersGroup.add(self.hero)
        self.handler.game.gameState.world.camera.centerOnEntity(self.hero)
        # self.hero = HeroKnight(self.handler)

    


    def keyManager(self):
        if self.handler.inputManager.pressed.get(pygame.K_d):
            self.hero.orderedToAttack = True
        else: self.hero.orderedToAttack = False
        if not self.hero.isAttacking :
        # and not self.hero.check_collision(self.handler.game.gameState.world.skeleton, self.playersGroup)
        # # not self.handler.game.gameState.circle.check_color_collision(self.hero, self.handler.game.gameState.objects)):
            if self.handler.inputManager.pressed.get(pygame.K_RIGHT) and self.hero.rect.x + self.hero.rect.width < 4000: #bg width
                self.hero.moveRight = True
            else: self.hero.moveRight = False
            if self.handler.inputManager.pressed.get(pygame.K_LEFT) and self.hero.rect.x > 0:
                self.hero.moveLeft = True
            else: self.hero.moveLeft = False
            if self.handler.inputManager.pressed.get(pygame.K_UP) and self.hero.rect.y > 0:
                self.hero.moveUp = True
            else: self.hero.moveUp = False
            if self.handler.inputManager.pressed.get(pygame.K_DOWN) and self.hero.rect.y + self.hero.rect.height < 1289: #bg height
                self.hero.moveDown = True
            else: self.hero.moveDown = False
        else: 
            self.hero.moveRight = False
            self.hero.moveLeft = False
            self.hero.moveUp = False
            self.hero.moveDown = False
        

    def tick(self):
        self.keyManager()
        self.handler.game.gameState.world.camera.centerOnEntity(self.hero)
        self.hero.tick()
        # self.handler.game.gameState.circle.check_color_collision(self.hero, self.handler.game.gameState.objects)

    def draw(self):
        self.hero.draw()