# from characterManager import CharacterManager
from inputManger import InputManager
# from enemyManager import EnemyManager
class Handler :

    def __init__(self, game):
        self.game = game

    def init (self):
        # self.characterManager = CharacterManager(self)
        self.inputManager = InputManager(self)
        # self.enemyManager = EnemyManager(self)