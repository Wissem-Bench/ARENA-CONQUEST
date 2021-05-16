from character import Character

class Skeleton(Character):
    
    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.skeleton, 100, 100, 5, 1)
        self.handler = handler
        self.name = 'skeleton'
        # self.moveRight = True
        # self.range