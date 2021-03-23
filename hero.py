import pygame
from animation import Animation

class Hero :
    
    def __init__(self, handler):
        self.handler = handler
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.heroAssets = self.handler.game.assets.heroNight
        self.currentAnimation = Animation(self.heroAssets.strip(False)[0:8], 0.05)
        self.rightIdleAnimation = Animation(self.heroAssets.strip(False)[0:8], 0.05)
        self.leftIdleAnimation = Animation(self.heroAssets.strip(True)[0:8], 0.05)
        self.rightRunAnimation = Animation(self.heroAssets.strip(False)[8:18], 0.05)
        self.leftRunAnimation = Animation(self.heroAssets.strip(True)[8:18], 0.05)
        self.rightAttackAnimation = Animation(self.heroAssets.strip(False)[18:25], 0.05)
        self.leftAttackAnimation = Animation(self.heroAssets.strip(True)[18:25], 0.05)
        self.rect = self.rightIdleAnimation.frames[0].get_rect()
        self.rect.x = 250
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

    # def keyManager(self):
        # bla bla bla

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


    # def last_side(self):
    #     # self.side = 'right'
    #     if self.handler.game.pressed.get(pygame.K_LEFT):
    #         self.side = 'left'
    #     elif handler.game.pressed.get(pygame.K_RIGHT):
    #         self.side = 'right'
    #     return side
