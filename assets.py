from spriteSheet import SpriteSheet 

class Assets:

    def __init__(self):
        self.heroNight = SpriteSheet("HeroKnight", 10, 9)
        self.skeleton = SpriteSheet("Skeleton Idle",11,1)
        self.skeletonWalk = SpriteSheet("skeleton walk",13,1)
        self.skeletonattack = SpriteSheet("skeleton Attack",18,1)

        
        
