import pygame
from animation import Animation
from character import Character
from player import Player

class Enemy(Character):

    def __init__(self, handler, asset, x, y):
        super().__init__(handler, asset, 30, 30, 5, 1)
        self.handler = handler
        # self.skeletonAssets = self.handler.game.assets.skeleton
        # self.skeletonWalkAssets = self.handler.game.assets.skeletonWalk
        # self.skeletonAttackAssets = self.handler.game.assets.skeletonattack
        # self.currentAnimation = Animation(self.skeletonAssets.strip(False)[0:11], 0.05)
        # self.rightIdleAnimation = Animation(self.skeletonAssets.strip(False)[0:11], 0.06)
        # self.leftIdleAnimation = Animation(self.skeletonAssets.strip(True)[0:11], 0.05)
        # self.rightRunAnimation = Animation(self.skeletonWalkAssets.strip(False)[0:13], 0.02)
        # self.leftRunAnimation = Animation(self.skeletonWalkAssets.strip(True)[0:13], 0.02)
        # self.rightAttackAnimation = Animation(self.skeletonAttackAssets.strip(False)[0:18], 0.05)
        # self.leftAttackAnimation = Animation(self.skeletonAttackAssets.strip(True)[0:18], 0.05)
        self.rect = self.rightIdleAnimation.frames[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.side = 'left'
        self.isAttacking = False
        self.isIdling = True
        # self.all_enemies = pygame.sprite.Group()




    def enemy_standard_move(self):
        if not self.handler.enemyManager.check_collision(self, self.handler.game.player.all_players):
            # il faut verifier le premier parametre de check collision(self) "de quel enemy on parle?"
            self.move_left()
    



    def animationManager(self):

        #closing attack animation
        if self.isAttacking:
            self.length = len(self.currentAnimation.frames)-1
            if self.currentAnimation.index == len(self.currentAnimation.frames)-1:
                self.isAttacking = False
                self.rightAttackAnimation.index = 0
                self.leftAttackAnimation.index = 0

        
        if not self.isAttacking:

            #idle animation
            if self.side == 'right':
                self.isIdling = True
                self.currentAnimation = self.rightIdleAnimation
            else: 
                self.currentAnimation = self.leftIdleAnimation

            #running animation
            if self.move_right() and self.rect.x + self.rect.width < self.handler.game.WIN.get_width():
                self.isIdling = False
                self.side = 'right'
                self.currentAnimation = self.rightRunAnimation

            if  self.enemy_standard_move() and self.rect.x > 0 :
                self.isIdling = False
                self.side = 'left'
                self.currentAnimation = self.leftRunAnimation
   
            if self.rect.y > 0:
                self.isIdling = False
                self.move_up()
                if self.side == 'right':
                    self.currentAnimation = self.rightRunAnimation
                else: self.currentAnimation = self.leftRunAnimation

            if self.rect.y + self.rect.height < self.handler.game.WIN.get_height():
                self.isIdling = False
                self.move_down()
                if self.side == 'right':
                    self.currentAnimation = self.rightRunAnimation
                else: self.currentAnimation = self.leftRunAnimation

        # attack animation
        # if "player is near to enemy" and not self.isAttacking:
        #     self.isAttacking = True
        #     if self.side == 'right':
        #         self.currentAnimation = self.rightAttackAnimation
        #     if self.side == 'left':
        #         self.currentAnimation = self.leftAttackAnimation

        




    def tick(self):
        self.animationManager()
        self.currentAnimation.tick()
        self.image = self.currentAnimation.getCurrentFrame()
        self.enemy_standard_move()


    def draw(self):
        self.handler.game.WIN.blit(self.currentAnimation.getCurrentFrame(), self.rect)