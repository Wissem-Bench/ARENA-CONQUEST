from character import Character

class HeroKnight(Character):

    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.heroknight, 100, 100, 10, 8)
        self.handler = handler
        self.name = "hero knight"

class EvilWizard(Character):

    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.evilwizard, 100, 100, 14, 1)
        self.handler = handler
        self.name = "evil wizard"

class Ronin(Character):

    def __init__(self, handler):
        super().__init__(handler, handler.game.assets.ronin, 100, 100, 12, 2)
        self.handler = handler
        self.name = "ronin"