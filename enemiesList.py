from character import Character

class Skeleton(Character):
    
    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.skeleton, 30, 30, 5, 3)
        self.handler = handler
        self.moveRight = True
        # self.range