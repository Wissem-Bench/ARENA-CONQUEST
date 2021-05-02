import pygame
from animation import Animation

class Character(pygame.sprite.Sprite) :
    
    def __init__(self, handler, assets, health, max_health, damage, velocity):
        super().__init__()
        self.handler = handler
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.velocity = velocity
        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False
        self.orderedToAttack = False
        self.rightIdleAnimation = Animation(assets[0], 0.07)
        self.leftIdleAnimation = Animation(assets[1], 0.07)
        self.rightRunAnimation = Animation(assets[2], 0.07)
        self.leftRunAnimation = Animation(assets[3], 0.07)
        self.rightAttackAnimation = Animation(assets[4], 0.05)
        self.leftAttackAnimation = Animation(assets[5], 0.05)
        self.currentAnimation = self.rightIdleAnimation
        self.rect = self.rightIdleAnimation.frames[0].get_rect()
        self.rect.x = 250
        self.rect.y = 250
        self.side = 'right'
        self.isAttacking = False
        # self.image = self.currentAnimation.frames[0]
        # self.mask = pygame.mask.from_surface(self.image)
        


    def move(self):
        if self.moveRight:
            self.rect.x += self.velocity

        if self.moveLeft:
            self.rect.x -= self.velocity

        if self.moveUp:
            self.rect.y -= self.velocity

        if self.moveDown:
            self.rect.y += self.velocity


    def animationManager(self):
    
        #closing attack animation
        if self.isAttacking:
            length = len(self.currentAnimation.frames)-1
            if self.currentAnimation.index == length:
                self.isAttacking = False
                # self.orderedToAttack = False # to prevent keep attacking using move keys
                self.rightAttackAnimation.index = 0
                self.leftAttackAnimation.index = 0

        
        # if not self.isAttacking:

            #running animation
        if self.moveRight:
            self.side = 'right'
            self.currentAnimation = self.rightRunAnimation

        if self.moveLeft:
            self.side = 'left'
            self.currentAnimation = self.leftRunAnimation

        if self.moveUp:
            if self.side == 'right':
                self.currentAnimation = self.rightRunAnimation
            else: self.currentAnimation = self.leftRunAnimation

        if self.moveDown:
            if self.side == 'right':
                self.currentAnimation = self.rightRunAnimation
            else: self.currentAnimation = self.leftRunAnimation

        # attack animation
        if (self.orderedToAttack and not self.isAttacking):
            self.isAttacking = True
            if self.side == 'right':
                self.currentAnimation = self.rightAttackAnimation
            if self.side == 'left':
                self.currentAnimation = self.leftAttackAnimation

        # idle animation
        if (all(key == False for key in self.handler.inputManager.pressed.values()) 
        and not self.isAttacking):
            if self.side == 'right':
                self.currentAnimation = self.rightIdleAnimation
            else: 
                self.currentAnimation = self.leftIdleAnimation


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        

    def tick(self):
        self.move()
        # self.moving = (self.moveRight or self.moveLeft or self.moveUp or self.moveDown)
        # print('moving: ' + str(self.moving))
        self.animationManager()
        self.currentAnimation.tick()
        # self.image = self.currentAnimation.getCurrentFrame()


    def draw(self):
        self.handler.game.WIN.blit(self.currentAnimation.getCurrentFrame(),
        (self.rect.x - self.handler.game.gameState.world.camera.xOffset,
        self.rect.y - self.handler.game.gameState.world.camera.yOffset))