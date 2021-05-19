import pygame, pygame.image, pygame.transform
import math
from spriteSheet import SpriteSheet 

class Assets:

    def __init__(self,handler):
        self.handler = handler
        # pass

    def initAssets(self):
        self.heroknight = self.parceling(SpriteSheet([["Hero Knight/HeroKnight", 10, 9]], (1, 1)), [8, 18, 24, 0, 46, 48, 49]) 
        #(46,48) for hurt animation
        #(49,58) for death

        self.evilwizard = self.parceling(SpriteSheet([["Evil Wizard/Idle2", 8, 1], 
                                                    ["Evil Wizard/Run2", 8, 1],
                                                    ["Evil Wizard/Attack2", 8, 1],
                                                    ["Evil Wizard/Take hit", 3, 1],
                                                    ["Evil Wizard/Death", 7, 1]], (1, 1)), [8,16,24,27,34])

        self.ronin = self.parceling(SpriteSheet([["Ronin/spr_RoninIdle_strip", 8, 1],
                                                ["Ronin/spr_RoninRun_strip", 10, 1],
                                                ["Ronin/spr_RoninAttack_strip", 25, 1],
                                                ["Ronin/spr_RoninGetHit_strip", 7, 1],
                                                ["Ronin/spr_RoninDeath_strip", 16, 1]], (1,1)), [8,18,43,50,66])

        self.skeleton = self.parceling(SpriteSheet([["Skeleton/Skeleton Idle", 11, 1], 
                                                    ["Skeleton/Skeleton Walk", 13, 1],
                                                    ["Skeleton/Skeleton Attack", 18, 1], #offset to attacking animation
                                                    ["Skeleton/Skeleton Hit", 8, 1],
                                                    ["Skeleton/Skeleton Dead", 15, 1]], (1,1)), [11,24,42,50,65])

        self.tower = self.parceling(SpriteSheet([["Tower/FlyingObelisk3", 13, 1], 
                                                ["Tower/FlyingObelisk3", 13, 1],
                                                ["Tower/lightning3", 13, 1],
                                                ["Tower/FlyingObelisk3", 13, 1],
                                                ["Tower/Destruction3", 17, 1]], (1,1)), [13,26,39,52,69])

        self.background = pygame.image.load("Assets/Menu/grey-cat-glacier.jpg").convert()
        self.background = pygame.transform.scale(self.background, (int(1920/2), int(1801/3)))

        self.grid = pygame.image.load("Assets/Menu/Grid.png")
        self.grid = pygame.transform.scale(self.grid, (300, 246))
        # self.grid.set_alpha(100)

        self.newGame = self.buttons("New game Button.png", 200, 60)
        self.newGame_rect = self.rect_pos(self.newGame, 18, 10)

        self.quit = self.buttons("Quit Button.png", 200, 60)
        self.quit_rect = self.rect_pos(self.quit, 18, 4)

        self.options = self.buttons("options Button.png", 200, 60)
        self.options_rect = self.rect_pos(self.options, 18, 2.5)

        self.start = self.buttons("Start Button.png", 200, 60)
        self.start_rect = self.rect_pos(self.start, 2.6, 1.8)

        self.back = self.buttons("Back Button.png", 200, 60)
        self.back_rect = self.rect_pos(self.back, 2.6, 1.4)

        self.right = self.buttons("Next Square Button.png", 100, 100)
        self.right_rect = self.rect_pos(self.right, 1.3, 5)

        self.left = self.buttons("Back Square Button.png", 100, 100)
        self.left_rect = self.rect_pos(self.left, 7, 5)

        # self.heroStart = pygame.image.load("Assets/Menu/")
        # self.heroFinishPoint = pygame.image.load("Assets/Menu/")
    
    def buttons(self, img, w, h):
        button = pygame.image.load(f"Assets/Menu/{img}")
        button = pygame.transform.scale(button, (w, h))
        return button

    def rect_pos(self, button, a, b):
        button_rect = button.get_rect()
        button_rect.x = math.ceil(self.handler.game.WIN.get_width()/a)
        button_rect.y = math.ceil(self.handler.game.WIN.get_height()/b)
        return button_rect

    # def parceling(self, spritesheet, indexes):
    #     result = []
    #     lastIndex = 0
    #     frames = spritesheet.strip()
    #     for index in indexes:
    #         result.append(frames[0][lastIndex: index])
    #         result.append(frames[1][lastIndex: index])
    #         lastIndex = index
    #     return result # array of arrays (group of frames)

    def parceling(self, spritesheet, indexes):
        result = []
        res = []
        lastIndex = 0
        frames = spritesheet.strip()
        ignore = False
        for index in indexes:
            if index != 0:
                if not ignore:
                    result.append(frames[0][lastIndex: index])
                    result.append(frames[1][lastIndex: index])
                    lastIndex = index
                    res.append(lastIndex)
                else:
                    ignore = False
                    lastIndex = index - 1
            else:
                ignore = True
        return result # array of arrays (group of frames)