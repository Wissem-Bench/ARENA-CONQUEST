import pygame
from heroesList import *



class Player:

    def __init__(self,handler):
        self.handler = handler
        self.hero = None
        # self.handler.characterManager.characterGroup.add(self.hero)
        # self.handler.characterManager.enemies.append(self.hero)
        self.handler.game.gameState.current_world.camera.centerOnEntity(self.hero)
        # self.hero.controller = self
        # self.handler.characterManager.
        


    # def player_health(self):
    #     if self.hero.collided :
    #         self.hero.damage(50)

    def keyManager(self):
        if self.handler.inputManager.pressed.get(pygame.K_d):
            self.hero.orderedToAttack = True
        else: self.hero.orderedToAttack = False
        if not self.hero.isAttacking and not self.hero.dead: 
            if self.handler.inputManager.pressed.get(pygame.K_RIGHT) and self.hero.rect.x + self.hero.rect.width < 3836: #bg width
                self.hero.moveRight = True
            else: self.hero.moveRight = False
            if self.handler.inputManager.pressed.get(pygame.K_LEFT) and self.hero.rect.x > 0:
                self.hero.moveLeft = True
            else: self.hero.moveLeft = False
            if self.handler.inputManager.pressed.get(pygame.K_UP) and self.hero.rect.y > 0:
                self.hero.moveUp = True
            else: self.hero.moveUp = False
            if self.handler.inputManager.pressed.get(pygame.K_DOWN) and self.hero.rect.y + self.hero.rect.height < 656: #bg height
                self.hero.moveDown = True
            else: self.hero.moveDown = False
        else: 
            self.hero.moveRight = False
            self.hero.moveLeft = False
            self.hero.moveUp = False
            self.hero.moveDown = False
        if self.handler.inputManager.pressed.get(pygame.K_s):
            self.hero.sprint = True
        else: self.hero.sprint = False
        if all(key == False for key in self.handler.inputManager.pressed.values()):
            self.hero.notOrdered = True
        else: self.hero.notOrdered = False

    def tick(self):
        self.keyManager()
        self.handler.game.gameState.current_world.camera.centerOnEntity(self.hero)
        self.hero.tick()
        # self.player_move()
        # self.handler.characterManager.check_rect_collision(self.hero, self.handler.characterManager.collided_entity(self.hero))
        # self.handler.game.gameState.circle.check_color_collision(self.hero, self.handler.game.gameState.objects)

    def draw(self):
        self.hero.draw()