import pygame, pygame.sprite
from enemiesList import Skeleton
from character import Character
import time

class CharacterManager():

    def __init__(self, handler):
        self.handler = handler

    def init(self):
        self.characterGroup = pygame.sprite.Group()
        self.enemies = []

    def enemy_spawn(self, character, x, y, world):
        character.rect.x = x
        character.rect.y = y
        # if self.handler.game.gameState.current_world == world :
        self.characterGroup.add(character)
        self.enemies.append(character.controller)

    def collided_entity(self, character):
        testing_group = pygame.sprite.Group()
        collide_group = pygame.sprite.Group()
        testing_group = self.characterGroup.copy()
        testing_group.remove(character)
        for entity in testing_group :
            if character.rect.colliderect(entity.rect):
                collide_group.add(entity)
                if not entity in character.rect_collision_side:
                    character.rect_collision_side.append(entity)
                    character.rect_collision_side.append('')
                    # print(f'collision of {character.name} is {character.rect_collision_side}')
        return collide_group

    def check_mask_collision(self): # test collision for all characters
        tempGroup = pygame.sprite.Group()
        for testingCharacter in self.characterGroup:
            tempGroup = self.characterGroup.copy()
            tempGroup.remove(testingCharacter)
            res = pygame.sprite.spritecollide(testingCharacter, tempGroup, False, pygame.sprite.collide_mask)
            if len(res) > 0:
                testingCharacter.collided = True
            else: testingCharacter.collided = False


    def check_rect_collision(self, character_1, character_2): #check_side_collision

        index = character_1.rect_collision_side.index(character_2)

        if abs(character_2.rect.top - character_1.rect.bottom) < 10:  #10 = collision tolarence
            character_1.rect_collision_side[index+1] = 'bottom'
        if abs(character_2.rect.bottom - character_1.rect.top) < 10: 
            character_1.rect_collision_side[index+1] = 'top'
        if abs(character_2.rect.right - character_1.rect.left) < 10: 
            character_1.rect_collision_side[index+1] = 'left'
        if abs(character_2.rect.left - character_1.rect.right) < 10: 
            character_1.rect_collision_side[index+1] = 'right'


    def check_characters_rect_collision(self):
        for character_1 in self.characterGroup: #for all characters
            for i in range(len(character_1.rect_collision_side)-2, 0, -2): #couples of (char, side)
                print(f'for {character_1.name} length {len(character_1.rect_collision_side)} index {i}')
                collidedChar = character_1.rect_collision_side[i] #for all its collided chars
                if not collidedChar.rect.contains(character_1.rect) and not character_1.rect.colliderect(collidedChar.rect):
                    # for removed in self.characterGroup:
                    #     if removed in character_1.rect_collision_side:
                    #         removedIndex = removed.rect_collision_side.index(character_1)
                    #         removed.rect_collision_side.remove(character_1)
                    #         removed.rect_collision_side.pop(removedIndex)
                    character_1.rect_collision_side.remove(collidedChar) #remove character that exit the rect
                    character_1.rect_collision_side.pop(i) #remove its appropriate side
            for character_2 in self.collided_entity(character_1):
                index = character_1.rect_collision_side.index(character_2)
                if character_1.rect_collision_side[index + 1] == '':
                    self.check_rect_collision(character_1, character_2)
                    
            
    def damage(self, character1: Character, character2: Character):

        if character1.isAttacking == True : 
            if  character1.rightCollide or character1.leftCollide or character1.topCollide or character1.downCollide:
                if character2 not in character1.hittingList:
                    character1.hittingList.append(character2)
                    if character2.health > 0:
                        character2.health -= character1.damage
                        character2.getHurt = True
                    if character1.damage > character2.health:
                        character2.health = 0
                        character2.dead = True
                        character2.getHurt = False
                        # self.characterGroup.remove(character2)
                        # self.enemies.remove(character2.controller)
        else: 
            del character1.hittingList[:]


    def tick(self):
        for enemy in self.enemies :
            enemy.tick()
        self.check_mask_collision()
        self.check_characters_rect_collision()
        for entity_1 in self.characterGroup:
            for entity_2 in self.characterGroup:
                if entity_1 is not entity_2:
                    self.damage(entity_1, entity_2)
    

    def draw(self):
        for enemy in self.enemies :
            enemy.draw()

    