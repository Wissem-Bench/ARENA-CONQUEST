from character import Character

class Skeleton(Character):
    
    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.skeleton, 100, 100, 5, 1, (5, 5))
        self.handler = handler
        self.name = 'skeleton'
        self.attack_rad = 20
        self.visual_rad = 160
        self.maxVelocity = 1.5
        # self.moveRight = True
        # self.range

class Tower(Character):
    
    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.tower, 100, 100, 15, 0, (-25, -35))
        self.handler = handler
        self.name = 'tower'
        self.leftIdleAnimation = self.rightIdleAnimation
        self.leftAttackAnimation = self.rightAttackAnimation
        self.leftDeathAnimation = self.rightDeathAnimation
        self.leftHurtAnimation = self.rightHurtAnimation
        self.leftRunAnimation = self.rightRunAnimation
        self.attack_rad = 150
        self.visual_rad = 150
        