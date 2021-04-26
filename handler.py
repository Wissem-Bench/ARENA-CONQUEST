# import pygame
# from playerManager import PlayerManager
from characterManager import CharacterManager
from inputManger import InputManager


class Handler :

    def __init__(self, game):
        self.game = game

    def init (self):
        self.characterManager = CharacterManager(self)
        self.inputManager = InputManager(self)