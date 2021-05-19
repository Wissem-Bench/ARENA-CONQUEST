import pygame
from animation import Animation

class Character(pygame.sprite.Sprite) :
    
    def __init__(self, handler, assets, health, max_health, damage, velocity, health_bar_offset):
        super().__init__()
        self.handler = handler
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.velocity = velocity
        self.maxVelocity = velocity*1.5
        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False
        self.rightCollide = False
        self.leftCollide = False
        self.topCollide = False
        self.downCollide = False
        self.orderedToAttack = False
        self.rightIdleAnimation = Animation(assets[0], 0.07)
        self.leftIdleAnimation = Animation(assets[1], 0.07)
        self.rightRunAnimation = Animation(assets[2], 0.07)
        self.leftRunAnimation = Animation(assets[3], 0.07)
        self.rightAttackAnimation = Animation(assets[4], 0.05)
        self.leftAttackAnimation = Animation(assets[5], 0.05)
        self.rightHurtAnimation = Animation(assets[6], 0.07)
        self.leftHurtAnimation = Animation(assets[7], 0.07)
        self.rightDeathAnimation = Animation(assets[8], 0.07)
        self.leftDeathAnimation = Animation(assets[9], 0.07)
        self.currentAnimation = self.rightIdleAnimation
        self.rect = self.rightRunAnimation.frames[0].get_rect()
        self.rect.x = 400 #player starting x (and y)
        self.rect.y = 250 
        self.side = 'right'
        self.isAttacking = False
        self.notOrdered = True
        self.WIN = self.handler.game.WIN
        self.image = self.currentAnimation.frames[0]
        self.collided = False
        self.rect_collision_side = []
        self.name = ''
        self.hittingList = []
        self.getHurt = False
        self.dead = False
        self.controller = None
        self.sprint = False
        self.visual_rad = 200
        self.attack_rad = 50
        self.health_bar_offset = health_bar_offset
        # self.positon = [self.rect.x, self.rect.y]
        # self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        # self.old_position = self.positon.copy()



    # def moving_range(self):
    #     if self.feet.collidelist(self.handler.game.gameState.world_1.walls) > -1:
    #         self.move_back()


    # def move_back(self):
    #     self.positon = self.old_position
    #     self.rect.topleft = self.positon
    #     self.feet.midbottom = self.rect.midbottom


    def health_bar(self, surface):
        x_camera_offset = self.handler.game.gameState.current_world.camera.xOffset
        y_camera_offset = self.handler.game.gameState.current_world.camera.yOffset
        # def health_bar(self, surface, xRectOffset, yRectOffset):
        Green = (111, 210, 46)
        Gray = (60, 60, 60)
        bar_position = [self.rect.x - x_camera_offset - self.health_bar_offset[0], self.rect.y - y_camera_offset - self.health_bar_offset[1], self.health, 2]
        back_bar_position = [self.rect.x - x_camera_offset - self.health_bar_offset[0], self.rect.y - y_camera_offset - self.health_bar_offset[1], self.max_health, 2]
        pygame.draw.rect(surface, Gray, back_bar_position)
        pygame.draw.rect(surface, Green, bar_position)


    def move(self):

        if self.collided and 'right' in self.rect_collision_side:
            self.rightCollide = True
        else: self.rightCollide = False
        if self.collided and 'left' in self.rect_collision_side:
            self.leftCollide = True
        else: self.leftCollide = False
        if self.collided and 'top' in self.rect_collision_side:
            self.topCollide = True
        else: self.topCollide = False
        if self.collided and 'bottom' in self.rect_collision_side:
            self.downCollide = True
        else: self.downCollide = False

        if self.moveRight and not self.rightCollide and self.rect.x + self.rect.width + self.velocity < self.handler.game.gameState.world_1.bg.get_rect().width:
            if self.sprint == True :
                self.rect.x += self.maxVelocity
            else : self.rect.x += self.velocity

        if self.moveLeft and not self.leftCollide and self.rect.x - self.velocity > 0:
            if self.sprint == True :
                self.rect.x -= self.maxVelocity
            else : self.rect.x -= self.velocity

        if self.moveUp and not self.topCollide and self.rect.y - self.velocity > 0:
            if self.sprint == True :
                self.rect.y -= self.maxVelocity
            else : self.rect.y -= self.velocity

        if self.moveDown and not self.downCollide and self.rect.y + self.rect.height + self.velocity < self.handler.game.gameState.world_1.bg.get_rect().height:
            if self.sprint == True :
                self.rect.y += self.maxVelocity
            else : self.rect.y += self.velocity
        
        # if ((self.moveRight and not self.rightCollide) or (self.moveLeft and not self.leftCollide) or (self.moveUp and  not self.topCollide) or (self.moveDown and not self.downCollide)) and self.sprint:
        #     self.velocity = self.maxVelocity
        #     print(str(self.velocity))
        
    def death(self):
        if self.dead:
            if self.currentAnimation == self.rightDeathAnimation or self.currentAnimation == self.leftDeathAnimation :
                if self.currentAnimation.index == len(self.currentAnimation.frames) - 1 :
                    self.handler.characterManager.characterGroup.remove(self)
                    self.handler.characterManager.enemies.remove(self.controller)


    def animationManager(self):

        # run animation
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
        #stopping attack animation
        if self.isAttacking:
            length = len(self.currentAnimation.frames)-1
            if self.currentAnimation.index == length:
                self.isAttacking = False
                # self.orderedToAttack = False # to prevent keep attacking using move keys
                self.rightAttackAnimation.index = 0
                self.leftAttackAnimation.index = 0

        # Hurt animation
        if self.getHurt == True :
            if self.side == 'right':
                self.currentAnimation = self.rightHurtAnimation
            else: 
                self.currentAnimation = self.leftHurtAnimation

            if self.rightHurtAnimation.index == len(self.rightHurtAnimation.frames)-1:
                self.rightHurtAnimation.index = 0
                self.getHurt = False
            if self.leftHurtAnimation.index == len(self.leftHurtAnimation.frames)-1:
                self.leftHurtAnimation.index = 0
                self.getHurt = False
                    # self.leftHurtAnimation.index = 0

        # death animation
        if self.dead == True :
            if self.side == 'right':
                self.currentAnimation = self.rightDeathAnimation
            else:
                self.currentAnimation = self.leftDeathAnimation
                
        # idle animation
        if (self.notOrdered and not self.dead and not self.getHurt and not self.isAttacking):
            if self.side == 'right':
                self.currentAnimation = self.rightIdleAnimation
            else: 
                self.currentAnimation = self.leftIdleAnimation


    def tick(self):
        self.death()
        self.move()
        self.animationManager()
        self.currentAnimation.tick()
        self.image = self.currentAnimation.getCurrentFrame()
        self.health_bar(self.WIN)
        # self.sprint()
        # self.moving_range()


    def draw(self):
        # pygame.draw.rect(self.WIN, (60, 60, 60), (self.rect.x - self.handler.game.gameState.current_world.camera.xOffset, self.rect.y - self.handler.game.gameState.current_world.camera.yOffset, self.rect.w, self.rect.h))
        pygame.draw.circle(self.WIN, (255, 0, 0), (self.rect.center[0] - self.handler.game.gameState.current_world.camera.xOffset, self.rect.center[1] - self.handler.game.gameState.current_world.camera.yOffset), self.visual_rad, 1)
        self.handler.game.WIN.blit(self.currentAnimation.getCurrentFrame(),
        (self.rect.x - self.handler.game.gameState.current_world.camera.xOffset,
        self.rect.y - self.handler.game.gameState.current_world.camera.yOffset))
        self.health_bar(self.WIN)
        pygame.draw.circle(self.WIN, (255, 0, 0), (self.rect.center[0] - self.handler.game.gameState.current_world.camera.xOffset, self.rect.center[1] - self.handler.game.gameState.current_world.camera.yOffset), 50, 1)