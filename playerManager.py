from player import Player
import pygame

class PlayerManager:

    def __init__(self, handler):
        self.handler = handler
        self.player = Player(self.handler)
        # self.player = Player(self.handler)
        self.player = self.handler.game.player
        self.all_players = pygame.sprite.Group()



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    # def players_appear(self):
    #     self.all_players.add(self.player)


    # def tick(self):
    #     for player in self.all_players:
    #         player.tick()

    # def draw(self):
    #     for player in self.all_players:
    #         player.draw()