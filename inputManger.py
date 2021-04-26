import pygame
import sys

class InputManager():

    def __init__(self,handler):
        self.handler = handler
        self.pressed = {}
        self.clicked = False
        self.pos = (0, 0)
        self.count = 0

    def tick(self):
        if self.clicked == True:
            self.clicked = False # :)
        self.pos = pygame.mouse.get_pos()
        self.check_events()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    print('game closed')
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
            elif event.type == pygame.MOUSEBUTTONUP:
                # if self.clicked == False:
                self.clicked = True