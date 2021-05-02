# from characterManager import CharacterManager
# from playerManager import PlayerManager
from character import Character


class GameCamera:

    def __init__(self, handler):
        self.handler = handler
        self.xOffset = 0
        self.yOffset = 0
        # self.background = self.handler.game.gameState.world.background

    def checkBlankSpace(self):
        if self.xOffset < 0:
            self.xOffset = 0
        elif self.xOffset > 4000 - self.handler.game.WIDTH: #1920 = background width
            self.xOffset = 4000 - self.handler.game.WIDTH

        if self.yOffset < 0:
            self.yOffset = 0
        elif self.yOffset > 1289 - self.handler.game.HEIGHT: #1289 = background height
            self.yOffset = 1289 - self.handler.game.HEIGHT
        
        
    def centerOnEntity(self, character):
        self.xOffset = character.rect.x - self.handler.game.WIDTH / 2 + character.rect.w / 2
        self.yOffset = character.rect.y - self.handler.game.HEIGHT / 2 + character.rect.h / 2
        # self.xOffset = character.rect.x - self.background.get_width() / 2 + character.rect.w / 2
        # self.yOffset = character.rect.y - self.background.get_height() / 2 + character.rect.h / 2
        self.checkBlankSpace()
        
    def move(xAmt, yAmt):
        self.xOffset += xAmt
        self.yOffset += yAmt
        self.checkBlankSpace()
