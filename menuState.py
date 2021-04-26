import pygame
import sys
from animation import Animation

class MenuState():
    
    def __init__(self, handler):
        self.handler = handler
        self.heroes = [self.handler.game.assets.heroknight, self.handler.game.assets.evilwizard]
        self.currentAnimation = Animation(self.heroes[0][0], 0.07)
        self.rect = self.currentAnimation.frames[0].get_rect()
        self.rect.x = 400
        self.rect.y = 100
        self.displayer = {
            "launch" : True ,
            "newgame" : False ,
            "options" : False
        }
        
        
    def init(self):
        self.handler.init()
        self.assets = self.handler.game.assets
        self.assets.initMenuAssets()
        
    def launch_draw(self):
        self.handler.game.WIN.blit(self.assets.background, (0, 0))
        self.handler.game.WIN.blit(self.assets.newGame, self.handler.game.assets.newGame_rect)
        self.handler.game.WIN.blit(self.assets.quit, self.handler.game.assets.quit_rect)
        self.handler.game.WIN.blit(self.assets.options, self.handler.game.assets.options_rect)

    def newGame_Draw(self):
        # self.handler.game.WIN.blit(self.assets.background, (0, 0))
        self.handler.game.WIN.blit(self.assets.grid, (300, 0)) #300=(900-300)/2
        self.handler.game.WIN.blit(self.assets.start, self.handler.game.assets.start_rect)
        self.handler.game.WIN.blit(self.assets.back, self.handler.game.assets.back_rect)
        self.handler.game.WIN.blit(self.assets.right, self.handler.game.assets.right_rect)
        self.handler.game.WIN.blit(self.assets.left, self.handler.game.assets.left_rect)
        self.handler.game.WIN.blit(self.currentAnimation.getCurrentFrame(), (self.rect.x, self.rect.y))

    def options_draw(self):
        self.handler.game.WIN.blit(self.assets.background, (0, 0))

    def check_event(self, button_rect):
        clicked == False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.assets.button_rect.collidepoint(event.pos):
                    print("ok")
                    clicked == True
                else: clicked == False
        return clicked

    def dict_initializer(self, dictionary, our_key):
        dictionary[our_key] = True
        for key in dictionary.keys():
            if key not in our_key:
                dictionary[key] = False

    # def hero_switcher(self):
    #     new variable to index animation, this var will be callable in current_draw(if right if left)              

    def current_draw(self):
        if self.handler.inputManager.clicked:
            
            if self.displayer["launch"] == True:
                if self.assets.newGame_rect.collidepoint(self.handler.inputManager.pos):
                    self.dict_initializer(self.displayer, "newgame")

                elif self.assets.options_rect.collidepoint(self.handler.inputManager.pos):
                    self.dict_initializer(self.displayer, "options")

                elif self.assets.quit_rect.collidepoint(self.handler.inputManager.pos):
                    running = False
                    pygame.quit()
                    print('game closed')
                    sys.exit()

            if self.displayer["newgame"] == True:

                if self.assets.right_rect.collidepoint(self.handler.inputManager.pos):
                    self.currentAnimation = Animation(self.heroes[1][0], 0.07)
                
                if self.assets.left_rect.collidepoint(self.handler.inputManager.pos):
                    self.currentAnimation = Animation(self.heroes[0][0], 0.07)

                if self.assets.start_rect.collidepoint(self.handler.inputManager.pos):
                    self.handler.game.currentState = self.handler.game.gameState
                
                if self.assets.back_rect.collidepoint(self.handler.inputManager.pos):
                    self.dict_initializer(self.displayer, "launch")

        if self.displayer["launch"] == True:
            self.launch_draw()
        elif self.displayer["newgame"] == True:
            self.newGame_Draw()
        elif self.displayer["options"] == True:
            self.options_draw()

    def draw(self):
        self.current_draw()

    def tick(self):
        self.currentAnimation.tick()