from character import Character
# from charactersList import Skeleton
from gameObject import GameObject
import pygame

class CharacterManager:

    def __init__(self, handler):
        self.handler = handler
        self.characterGroup = pygame.sprite.Group()
        # self.skeleton = Skeleton(self.handler)

        # injecting handler to every instantiated character
        # self.character = Character(self.handler)
        # self.skeleton = Skeleton(self.handler)


        # self.characterGroup = pygame.sprite.Group()
        # self.characterscharacterGroup_appear(500, 200)
        # self.characterscharacterGroup_appear(500, 250)



    # def characterscharacterGroup_appear(self, x, y):
    #     self.character = character(self.handler, self.handler.game.assets.skeleton, x, y)
    #     self.characterGroup.add(self.character)


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        


    def character_spawn(self, character, x, y):
        # self.character = Character(self.handler, self.handler.game.assets.skeleton, x, y)
        character.rect.x = x
        character.rect.y = y
        self.characterGroup.add(character)

    def tick(self):
        for character in self.characterGroup:
            character.tick()

    def draw(self):
        # for character in self.characterGroup:
            # character.draw()
        # self.character_spawn(self.skeleton, 240,200)
        pass