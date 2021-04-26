import pygame
from charactersList import HeroKnight
from charactersList import EvilWizard



class Player:

    def __init__(self,handler):
        self.handler = handler
        self.character = HeroKnight(self.handler)
        self.handler.game.gameState.camera.centerOnEntity(self.character)
        # self.all_players = pygame.sprite.Group()



    # heroknight = Player(handler,heroknight)
    # heroknight.rightIdleAnimation =

    def keyManager(self):
        if self.handler.inputManager.pressed.get(pygame.K_d):
            self.character.orderedToAttack = True
        else: self.character.orderedToAttack = False
        if not self.character.isAttacking:
            # if not self.handler.characterManager.check_collision(self.character, self.handler.characterManager.characterGroup):
            if not self.handler.game.gameState.circle.check_color_collision(self.character, self.handler.game.gameState.objects):
                if self.handler.inputManager.pressed.get(pygame.K_RIGHT):
                # and self.character.rect.x + self.character.rect.width < self.handler.game.WIN.get_width()):
                    self.character.moveRight = True
                else: self.character.moveRight = False
                if self.handler.inputManager.pressed.get(pygame.K_LEFT):
                # and self.character.rect.x > 0:
                    self.character.moveLeft = True
                else: self.character.moveLeft = False
                if self.handler.inputManager.pressed.get(pygame.K_UP): 
                # and self.character.rect.y > 0:
                    self.character.moveUp = True
                else: self.character.moveUp = False
                if self.handler.inputManager.pressed.get(pygame.K_DOWN):
                # and self.character.rect.y + self.character.rect.height < self.handler.game.WIN.get_height()):
                    self.character.moveDown = True
                else: self.character.moveDown = False
        else: 
            self.character.moveRight = False
            self.character.moveLeft = False
            self.character.moveUp = False
            self.character.moveDown = False
        

    def tick(self):
        self.keyManager()
        self.handler.game.gameState.camera.centerOnEntity(self.character)
        self.character.tick()

    def draw(self):
        self.character.draw()

