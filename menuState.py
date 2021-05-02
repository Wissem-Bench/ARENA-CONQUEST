import pygame
import sys
from animation import Animation
from heroesList import *

class MenuState():
    
    def __init__(self, handler):
        self.handler = handler
        
        
    def init(self):
        self.handler.init()
        self.assets = self.handler.game.assets
        self.assets.initMenuAssets()
        self.assets.initGameAssets()
        self.heroes = [self.handler.game.assets.heroknight, self.handler.game.assets.evilwizard, self.handler.game.assets.ronin]
        self.currentAnimation = Animation(self.heroes[0][0], 0.07)
        self.rect = self.currentAnimation.frames[0].get_rect()
        self.rect.x = 400 # plutot une equation correctif pour toute autre entité (et de mm pour y)
        self.rect.y = 100 # pour Evil Wizard x =~ 300 et y =~ 20
        self.displayer = {
            "launch" : True ,
            "newgame" : False ,
            "options" : False
        }
        self.choosenHero = HeroKnight(self.handler)
        
    def launch_draw(self):
        self.handler.game.WIN.blit(self.assets.background, (0, 0))
        self.handler.game.WIN.blit(self.assets.newGame, self.assets.newGame_rect)
        self.handler.game.WIN.blit(self.assets.quit, self.assets.quit_rect)
        self.handler.game.WIN.blit(self.assets.options, self.assets.options_rect)

    def newGame_Draw(self):
        # self.handler.game.WIN.blit(self.assets.background, (0, 0))
        self.handler.game.WIN.blit(self.assets.grid, (300, 0)) #300=(900-300)/2
        self.handler.game.WIN.blit(self.assets.start, self.assets.start_rect)
        self.handler.game.WIN.blit(self.assets.back, self.assets.back_rect)
        self.handler.game.WIN.blit(self.assets.right, self.assets.right_rect)
        self.handler.game.WIN.blit(self.assets.left, self.assets.left_rect)
        self.handler.game.WIN.blit(self.currentAnimation.getCurrentFrame(), (self.rect.x, self.rect.y))

    def options_draw(self):
        self.handler.game.WIN.blit(self.assets.background, (0, 0))
        self.handler.game.WIN.blit(self.assets.back, self.assets.back_rect)


    def dict_initializer(self, dictionary, our_key):
        dictionary[our_key] = True
        for key in dictionary.keys():
            if key not in our_key:
                dictionary[key] = False

    def check_clicked_button(self, button_rect):
        if self.handler.inputManager.clicked:
            return True if button_rect.collidepoint(self.handler.inputManager.pos) else False             

    def current_draw(self):
        if self.displayer["launch"] == True:
            if self.check_clicked_button(self.assets.newGame_rect):
                self.dict_initializer(self.displayer, "newgame")

            elif self.check_clicked_button(self.assets.options_rect):
                self.dict_initializer(self.displayer, "options")

            elif self.check_clicked_button(self.assets.quit_rect):
                running = False
                pygame.quit()
                print('game closed')
                sys.exit()

        if self.displayer["newgame"] == True:

            if self.check_clicked_button(self.assets.right_rect):
                self.currentAnimation = Animation(self.heroes[1][0], 0.07)

                if self.check_clicked_button(self.assets.right_rect):
                    self.currentAnimation = Animation(self.heroes[2][0], 0.07)
            
            if self.check_clicked_button(self.assets.left_rect):
                self.currentAnimation = Animation(self.heroes[0][0], 0.07)

            if self.check_clicked_button(self.assets.start_rect):
                self.handler.game.gameState.player.hero = self.choosenHero
                self.handler.game.currentState = self.handler.game.gameState
                return
            
            if self.check_clicked_button(self.assets.back_rect):
                self.dict_initializer(self.displayer, "launch")

        if self.displayer["options"] == True:
            if self.check_clicked_button(self.assets.back_rect):
                self.dict_initializer(self.displayer, "launch")

        if self.displayer["launch"] == True:
            self.launch_draw()
        elif self.displayer["newgame"] == True:
            self.newGame_Draw()
        elif self.displayer["options"] == True:
            self.options_draw()


    # def index(self):
    #     print("inside defffffffffffffffff")
    #     if self.handler.inputManager.clicked:
    #         print("inside clickeeeeeed")
    #         if self.assets.right_rect.collidepoint(self.handler.inputManager.pos):
    #             print("rightttttttttttttttt")



    def changeHero(self):
        if self.check_clicked_button(self.assets.right_rect):
            self.choosenHero = EvilWizard(self.handler)
            self.rect.x = 320
            self.rect.y = 0.5
            print('1')

            if self.check_clicked_button(self.assets.right_rect):
                self.choosenHero = Ronin(self.handler)
                self.rect.x = 320
                self.rect.y = 0.5
                print('3')

        if self.check_clicked_button(self.assets.left_rect):
            self.choosenHero = HeroKnight(self.handler)
            print('2')
            self.rect.x = 400
            self.rect.y = 100
        # self.index()
        #     if self.displayer["newgame"] == True:
        #         print("displayer true")
        #             character = EvilWizard(self.handler)
        #             print("evilwizard")
        #         if self.assets.left_rect.collidepoint(self.handler.inputManager.pos):
        #             character = HeroKnight(self.handler)
        #             print("heroknight")
        #         if self.assets.start_rect.collidepoint(self.handler.inputManager.pos):
        #             character = EvilWizard(self.handler)
        #             print("evil start")

    def draw(self):
        self.current_draw()

    def tick(self):
        self.currentAnimation.tick()
        self.changeHero()