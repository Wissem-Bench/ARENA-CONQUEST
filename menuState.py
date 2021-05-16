import pygame
import sys
from animation import Animation
from heroesList import *
from itertools import cycle

class MenuState():
    
    def __init__(self, handler):
        self.handler = handler
        
        
    def init(self):
        self.handler.init()
        self.assets = self.handler.game.assets
        self.assets.initAssets()
        self.heroes = [Animation(self.handler.game.assets.heroknight[0], 0.07), 
                        Animation(self.handler.game.assets.evilwizard[2], 0.07), 
                        Animation(self.handler.game.assets.ronin[0], 0.07)]
        self.currentAnimation = self.heroes[0]
        self.choosenHero = self.heroes.index(self.currentAnimation)
        self.rect = self.currentAnimation.frames[0].get_rect()
        # self.rect.center = (450 , 0)
        self.rect.x = 300 + self.assets.grid.get_rect().w / 2 - self.rect.w / 2
        self.rect.y = 0 + self.assets.grid.get_rect().h / 2 - self.rect.h / 2
        self.displayer = {
            "launch" : True,
            "newgame" : False,
            "options" : False
        }

    def page_draw(self, page_name):
        if page_name == "launch":
            self.elements_draw([[self.assets.background, (0, 0)], 
                                [self.assets.newGame, self.assets.newGame_rect],
                                [self.assets.quit, self.assets.quit_rect],
                                [self.assets.options, self.assets.options_rect]])
        elif page_name == "newgame":
            self.elements_draw([[self.assets.grid, (300, 0)], 
                                [self.assets.start, self.assets.start_rect],
                                [self.assets.back, self.assets.back_rect],
                                [self.assets.right, self.assets.right_rect],
                                [self.assets.left, self.assets.left_rect],
                                [self.currentAnimation.getCurrentFrame(), (self.rect.x, self.rect.y)]])
        elif page_name == "options":
            self.elements_draw([[self.assets.background, (0, 0)], 
                                [self.assets.back, self.assets.back_rect]])
    
    def elements_draw(self, elements):
        for i in elements:
            self.handler.game.WIN.blit(i[0], i[1])


    def switch_displayer(self, our_key):
        for key in self.displayer.keys():
            self.displayer[key] = False
        self.displayer[our_key] = True

    def check_clicked_button(self, button_rect):
        if self.handler.inputManager.clicked:
            if button_rect.collidepoint(self.handler.inputManager.pos):
                return True
        return False

    def current_tick(self):
        if self.displayer["launch"]:
            if self.check_clicked_button(self.assets.newGame_rect):
                self.switch_displayer("newgame")

            elif self.check_clicked_button(self.assets.options_rect):
                self.switch_displayer("options")

            elif self.check_clicked_button(self.assets.quit_rect):
                pygame.quit()
                print('game closed')
                sys.exit()

        elif self.displayer["newgame"]:

            if self.check_clicked_button(self.assets.right_rect):
                self.choosenHero += 1
                if self.choosenHero >= len(self.heroes):
                    self.choosenHero = 0
            
            if self.check_clicked_button(self.assets.left_rect):
                self.choosenHero -= 1
                if self.choosenHero < 0:
                    self.choosenHero = len(self.heroes) - 1

            self.currentAnimation = self.heroes[self.choosenHero]

            if self.check_clicked_button(self.assets.start_rect):
                self.handler.game.gameState.player.hero = self.playerHero()
                self.handler.characterManager.characterGroup.add(self.handler.game.gameState.player.hero)
                self.handler.game.currentState = self.handler.game.gameState
                return
            
            if self.check_clicked_button(self.assets.back_rect):
                self.switch_displayer("launch")

        elif self.displayer["options"] == True:
            if self.check_clicked_button(self.assets.back_rect):
                self.switch_displayer("launch")

    def playerHero(self):
        if self.choosenHero == 0:
            return HeroKnight(self.handler)
            # self.rect.x = 400
            # self.rect.y = 100

        elif self.choosenHero == 1:
            return EvilWizard(self.handler)
            # self.rect.x = 320
            # self.rect.y = 0.5

        elif self.choosenHero == 2:
            return Ronin(self.handler)
            # self.rect.x = 320
            # self.rect.y =50

    def draw(self):
        currentdisplayer = ""
        for k, v in self.displayer.items():
            if v == True:
                currentdisplayer = k
        self.page_draw(currentdisplayer)

    def tick(self):
        self.current_tick()
        self.currentAnimation.tick()