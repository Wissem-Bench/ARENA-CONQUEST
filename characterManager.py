from character import Character
import pygame

class CharacterManager:

    def __init__(self, handler):
        self.handler = handler
        self.all_characters = pygame.sprite.Group()


        # self.all_characters = pygame.sprite.Group()
        # self.charactersall_characters_appear(500, 200)
        # self.charactersall_characters_appear(500, 250)



    # def charactersall_characters_appear(self, x, y):
    #     self.character = character(self.handler, self.handler.game.assets.skeleton, x, y)
    #     self.all_characters.add(self.character)
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    def character_spawn(self, x, y):
        self.character = Character(self.handler, self.handler.game.assets.skeleton, x, y)
        self.all_characters.add(self.character)

    def tick(self):
        for character in self.all_characters:
            character.tick()

    def draw(self):
        for character in self.all_characters:
            character.draw()