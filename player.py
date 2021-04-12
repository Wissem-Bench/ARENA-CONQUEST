import pygame

class Player:

    def __init__(self,handler,character):
        # super().__init__(handler,asset,100,100,10,5)
        self.handler = handler
        self.character = character
        # self.all_players = pygame.sprite.Group()



    # heroknight = Player(handler,heroknight)
    # heroknight.rightIdleAnimation =

    def keyManager(self):
        if not self.handler.characterManager.check_collision(self.character, self.handler.characterManager.all_characters):
            if self.handler.game.pressed.get(pygame.K_RIGHT):
                self.character.moveRight = True
                self.character.rect.x += self.character.velocity
            else: self.character.moveRight = False
            if self.handler.game.pressed.get(pygame.K_LEFT):
                self.character.moveLeft = True
                self.character.rect.x -= self.character.velocity
            else: self.character.moveLeft = False
            if self.handler.game.pressed.get(pygame.K_UP):
                self.character.moveUp = True
                self.character.rect.y -= (self.character.velocity*0.60)
            else: self.character.moveUp = False
            if self.handler.game.pressed.get(pygame.K_DOWN):
                self.character.moveDown = True
                self.character.rect.y += (self.character.velocity*0.60)
            else: self.character.moveDown = False
        

    

    def tick(self):
        self.keyManager()


    # def draw(self):
    #     self.handler.game.WIN.blit(self.currentAnimation.getCurrentFrame(), self.rect)


    # def last_side(self):
    #     # self.side = 'right'
    #     if self.handler.game.pressed.get(pygame.K_LEFT):
    #         self.side = 'left'
    #     elif handler.game.pressed.get(pygame.K_RIGHT):
    #         self.side = 'right'
    #     return side
