# from characterManager import CharacterManager
# from playerManager import PlayerManager
from character import Character


class GameCamera:

    def __init__(self, handler):
        self.handler = handler
        self.xOffset = 0
        self.yOffset = 0

    def checkBlankSpace(self):
        if self.xOffset < 0:
            self.xOffset = 0
        elif self.xOffset > 10500 - self.handler.game.WIDTH:
            self.xOffset = 10500 - self.handler.game.WIDTH

        if self.yOffset < 0:
            self.yOffset = 0
        elif self.yOffset > 6000 - self.handler.game.WIDTH:
            self.yOffset = 6000 - self.handler.game.WIDTH
        
        
    def centerOnEntity(self, character):
        self.xOffset = character.rect.x - self.handler.game.WIDTH / 2 + character.rect.w / 2
        self.yOffset = character.rect.y - self.handler.game.HEIGHT / 2 + character.rect.h / 2
        self.checkBlankSpace()
        
    def move(xAmt, yAmt):
        self.xOffset += xAmt
        self.yOffset += yAmt
        self.checkBlankSpace()
