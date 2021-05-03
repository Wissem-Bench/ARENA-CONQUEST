from character import Character

class HeroKnight(Character):

    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.heroknight, 100, 100, 10, 5)
        self.handler = handler

class EvilWizard(Character):

    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.evilwizard, 100, 100, 14, 7)
        self.handler = handler

class Ronin(Character):

    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.ronin, 100, 100, 12, 8)
        self.handler = handler
        