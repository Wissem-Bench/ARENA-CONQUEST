import pygame
from characterManager import CharacterManager
# from playerManager import PlayerManager


class Handler :

    def __init__(self, game):
        self.game = game
        # self.enemyManager = EnemyManager(self)

    def init (self):
        self.characterManager = CharacterManager(self)
        # self.playerManager = PlayerManager(self)