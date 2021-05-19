from character import Character

class Skeleton(Character):
    
    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.skeleton, 30, 30, 5, 1, (5, 5))
        self.handler = handler
        self.name = 'skeleton'
        # self.moveRight = True
        # self.range

class Tower(Character):
    
    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.tower, 100, 100, 0, 0, (-25, -35))
        self.handler = handler
        self.name = 'tower'