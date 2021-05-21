import pygame
import math
import utils
import random
import time

class EnemyController():
    
    def __init__(self, handler, character):
        self.handler = handler
        self.character = character
        self.character.controller = self
        self.lastRandomMoveTime, self.currentRandomMoveTime, self.randomMoveTimer = 0,0,0
        self.randomMoveLimitTime = 0
        self.lastCooldownTime, self.currentCooldownTime, self.cooldownTimer = 0,0,0
        self.randomMovingState = True
        self.coolingDownState = False
        self.chasingState = False
        self.attackingState = False

    def behave(self):
        if (not self.character.moveRight and not self.character.moveLeft and not self.character.moveUp 
        and not self.character.moveDown and not self.character.orderedToAttack):
            self.character.notOrdered = True
        else: self.character.notOrdered = False
        if not self.character.isAttacking and not self.character.dead and not self.character.getHurt:
            if not self.inVisualRange(self.handler.game.gameState.player.hero):
                self.character.sprint = False
                if self.chasingState:
                    self.coolingDownState = True
                    self.randomMovingState = False
                    self.lastCooldownTime = time.time()
                    self.chasingState = False
                    print('start cooldown')
                else:
                    self.randomMove()
                    print('random')
                self.attackingState = False # for long attack animation (outside circle but still attacking)
            else:
                self.character.sprint = True
                self.chasing(self.handler.game.gameState.player.hero)
        if self.attackingState:
            self.stopMoving()
            self.character.orderedToAttack = True
            print('attacking')
        else: self.character.orderedToAttack = False

    def inVisualRange(self, enemy):
        if utils.isInside(self.character.rect.center[0] , self.character.rect.center[1], self.character.visual_rad, enemy.rect.center[0], enemy.rect.center[1]):
            return True
        return False

    def stopMoving(self):
        self.character.moveRight = False
        self.character.moveLeft = False
        self.character.moveUp = False
        self.character.moveDown = False
        
    def cooldownAfterChasing(self):
        print('cooldown')
        self.currentCooldownTime = time.time()
        self.cooldownTimer = self.currentCooldownTime - self.lastCooldownTime
        print(f'cooldown: {self.cooldownTimer}')
        if self.cooldownTimer < 0.2:
            self.stopMoving()
        else:
            self.coolingDownState = False
            self.randomMovingState = True

    def randomMove(self):
        
        if not self.randomMovingState:
            self.cooldownAfterChasing()
        else:
        
            if self.handler.characterManager.blocked(self.character):
                self.stopMoving()
                self.randomMoveTimer = 0
                self.randomMoveLimitTime = 0
            if self.randomMoveLimitTime > 0:
                self.currentRandomMoveTime = time.time()
                self.randomMoveTimer = self.currentRandomMoveTime - self.lastRandomMoveTime
                if self.randomMoveTimer > self.randomMoveLimitTime:
                    self.lastRandomMoveTime = self.currentRandomMoveTime
                    self.randomMoveTimer = 0
                    self.randomMoveLimitTime = 0
            else:
                self.stopMoving()
                direction = random.randint(1, 8)
                self.randomMoveLimitTime = random.uniform(1.5, 4)
                if direction == 1:
                    self.character.moveRight = True
                elif direction == 2:
                    self.character.moveLeft = True
                elif direction == 3:
                    self.character.moveUp = True
                elif direction == 4:
                    self.character.moveDown = True
                elif direction == 5:
                    self.character.moveRight = True
                    self.character.moveUp = True
                elif direction == 6:
                    self.character.moveLeft = True
                    self.character.moveUp = True
                elif direction == 7:
                    self.character.moveRight = True
                    self.character.moveDown = True
                elif direction == 8:
                    self.character.moveLeft = True
                    self.character.moveDown = True
                self.currentRandomMoveTime = time.time()
                self.lastRandomMoveTime = time.time()


    def chasing(self, enemy):
        enemyX = enemy.rect.center[0]
        enemyY = enemy.rect.center[1]
        actualX = self.character.rect.center[0]
        actualY = self.character.rect.center[1]
        
        if utils.isInside(actualX, actualY, self.character.attack_rad, enemyX, enemyY):
            self.stopMoving()
            self.chasingState = False
            self.attackingState = True
            return
        else: 
            self.chasingState = True
            self.attackingState = False
            print('chasing')
        
        if actualX < enemyX - enemy.velocity:
            self.character.moveRight = True
        else: self.character.moveRight = False
        
        if actualX > enemyX + enemy.velocity:
            self.character.moveLeft = True
        else: self.character.moveLeft = False
        
        if actualY < enemyY - enemy.velocity:
            self.character.moveDown = True
        else: self.character.moveDown = False
        
        if actualY > enemyY + enemy.velocity:
            self.character.moveUp = True
        else: self.character.moveUp = False
    
    def tick(self):
        self.character.tick()
        self.behave()
        

    def draw(self):
        self.character.draw()