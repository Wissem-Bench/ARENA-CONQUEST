import pygame
from animation import Animation
from hero import Hero

class Enemy(Hero):
    def __init__(self,handler):
        super().__init__(handler)
        self.handler = handler
        self.health = 30
        self.max_health = 30
        self.attack = 5
        self.velocity = 3
        self.skeletonAssets = self.handler.game.assets.skeleton
        self.skeletonWalkAssets = self.handler.game.assets.skeletonWalk
        self.skeletonAttackAssets = self.handler.game.assets.skeletonattack
        self.currentAnimation = Animation(self.skeletonAssets.strip(False)[0:11], 0.05)
        self.rightIdleAnimation = Animation(self.skeletonAssets.strip(False)[0:11], 0.05)
        self.leftIdleAnimation = Animation(self.skeletonAssets.strip(True)[0:11], 0.05)
        self.rightRunAnimation = Animation(self.skeletonWalkAssets.strip(False)[0:13], 0.05)
        self.leftRunAnimation = Animation(self.skeletonWalkAssets.strip(True)[0:13], 0.05)
        self.rightAttackAnimation = Animation(self.skeletonAttackAssets.strip(False)[0:18], 0.05)
        self.leftAttackAnimation = Animation(self.skeletonAttackAssets.strip(True)[0:18], 0.05)
        self.rect = self.rightIdleAnimation.frames[0].get_rect()
        self.rect.x = 500
        self.rect.y = 200
        self.side = 'right'
        self.isAttacking = False


    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity



    def animationManager(self):

        #closing attack animation
        if self.isAttacking:
            self.length = len(self.currentAnimation.frames)-1
            if self.currentAnimation.index == len(self.currentAnimation.frames)-1:
                self.isAttacking = False
                self.rightAttackAnimation.index = 0
                self.leftAttackAnimation.index = 0

        
        if not self.isAttacking:

            #running animation
            if (self.handler.game.pressed.get(pygame.K_RIGHT)
            and self.rect.x + self.rect.width < self.handler.game.WIN.get_width()):
                self.side = 'right'
                self.move_right()
                self.currentAnimation = self.rightRunAnimation
            if self.handler.game.pressed.get(pygame.K_LEFT) and self.rect.x > 0:
                self.side = 'left'
                self.move_left()
                self.currentAnimation = self.leftRunAnimation
   
            if self.handler.game.pressed.get(pygame.K_UP) and self.rect.y > 0:
                self.move_up()
                if self.side == 'right':
                    self.currentAnimation = self.rightRunAnimation
                else: self.currentAnimation = self.leftRunAnimation
            if (self.handler.game.pressed.get(pygame.K_DOWN) 
                and self.rect.y + self.rect.height < self.handler.game.WIN.get_height()):
                self.move_down()
                if self.side == 'right':
                    self.currentAnimation = self.rightRunAnimation
                else: self.currentAnimation = self.leftRunAnimation

        # attack animation
        if (self.handler.game.pressed.get(pygame.K_d)
        and not self.isAttacking):
            self.isAttacking = True
            if self.side == 'right':
                self.currentAnimation = self.rightAttackAnimation
            if self.side == 'left':
                self.currentAnimation = self.leftAttackAnimation

        # idle animation
        if (all(key == False for key in self.handler.game.pressed.values()) 
        and not self.isAttacking):
            if self.side == 'right':
                self.currentAnimation = self.rightIdleAnimation
            else: 
                self.currentAnimation = self.leftIdleAnimation


    def tick(self):
        self.animationManager()
        self.currentAnimation.tick()


    def draw(self):
        self.handler.game.WIN.blit(self.currentAnimation.getCurrentFrame(), self.rect)