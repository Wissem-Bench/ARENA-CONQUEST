from character import Character

class HeroKnight(Character):

    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.heroknight, 100, 100, 10, 5)
        self.handler = handler

class EvilWizard(Character):

    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.evilwizard, 100, 100, 10, 5)
        self.handler = handler

# class Skeleton(Character):
    
#     def __init__(self, handler):
#         super().__init__(handler, handler.game.assets.skeleton, 30, 30, 5, 3)
#         self.handler = handler