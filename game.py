
from hero import Hero
from enemy import Enemy
from handler import Handler
import pygame
import sys
from assets import Assets
pygame.init()

class Game:

    def __init__(self):
        pygame.display.set_caption("My Game")
        self.FPS = 60
        self.WIDTH = 900
        self.HEIGHT = 500
        self.WIN = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.dest = (100, 100)
        self.handler = Handler(self) # should be before any other object that have handler in its const.
        self.assets = Assets()
        self.hero = Hero(self.handler)
        self.enemy = Enemy(self.handler)
        self.pressed = {
            "right key" : False,
            "left key" : False,
            "up key" : False,
            "down key" : False,
            "d key" : False
        }

    def draw_window(self):
        self.WIN.fill(self.BLACK)
        # draw everything here:
        self.hero.draw()
        self.enemy.draw()
        
        # end of drawing
        pygame.display.flip()
        

    def tick(self):
        self.hero.tick()
        self.enemy.tick()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.FPS)
            self.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    print('game closed')
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    self.pressed[event.key] = False
            self.draw_window()