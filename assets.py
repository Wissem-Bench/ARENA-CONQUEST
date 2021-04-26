import pygame
import math
from spriteSheet import SpriteSheet 

class Assets:

    def __init__(self,handler):
        self.handler = handler
        # pass

    def initGameAssets(self):
        self.bg = pygame.image.load("Assets/grey-cat-8.jpg").convert()
        # self.bg = pygame.transform.scale(self.bg, (int(8400/7), int(4500/7)))

        self.heroknight = self.parceling(SpriteSheet([["HeroKnight", 10, 9]]), [8, 18, 24])

        self.evilwizard = self.parceling(SpriteSheet([["Evil Wizard/Idle", 8, 1], 
                                                    ["Evil Wizard/Run", 13, 1],
                                                    ["Evil Wizard/Attack1", 18, 1]]), [8,16,24])

        self.skeleton = self.parceling(SpriteSheet([["Skeleton Idle", 11, 1], 
                                                    ["Skeleton Walk", 13, 1],
                                                    ["Skeleton Attack", 18, 1]]), [11, 24, 42])

    def initMenuAssets(self):
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
    
    def buttons(self, img, w, h):
        button = pygame.image.load(f"Assets/Menu/{img}")
        button = pygame.transform.scale(button, (w, h))
        return button

    def rect_pos(self, button, a, b):
        button_rect = button.get_rect()
        button_rect.x = math.ceil(self.handler.game.WIN.get_width()/a)
        button_rect.y = math.ceil(self.handler.game.WIN.get_height()/b)
        return button_rect

    def parceling(self, spritesheet, indexes):
        result = []
        lastIndex = 0
        frames = spritesheet.strip()
        for index in indexes:
            result.append(frames[0][lastIndex: index])
            result.append(frames[1][lastIndex: index])
            lastIndex = index
        return result # array of arrays (group of frames)