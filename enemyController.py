import pygame
import math
import utils

class EnemyController():
    
    def __init__(self, handler, character):
        self.handler = handler
        self.character = character
        self.character.controller = self
        # self.enemy_collision_side = self.handler.characterManager.check_rect_collision(self.character.rect, self.handler.characterManager.collided_entity(self.character))
        # moveZone = self.circle(moveZone)
        # followingZone = self.circle(followingZone)
        # attackingZone = self.circle(attackingZone)

    def behave(self):
        if (not self.character.moveRight and not self.character.moveLeft and not self.character.moveUp 
        and not self.character.moveDown and not self.character.orderedToAttack):
            self.character.notOrdered = True
        else: self.character.notOrdered = False
        if self.character.name == "ronin":
            if not self.character.isAttacking and not self.character.dead and not self.character.getHurt:
                    self.character.moveLeft = True
            else: self.character.moveLeft = False
        elif self.character.name == "skeleton":
            if not self.character.isAttacking and not self.character.dead and not self.character.getHurt:
                    self.character.moveRight = True
            else: self.character.moveRight = False
        elif self.character.name == "evil wizard":
            if not self.character.isAttacking and not self.character.dead and not self.character.getHurt:
                    self.character.moveLeft = True
            else: self.character.moveLeft = False


    def isInside(circle_x, circle_y, rad, x, y):
        if ((x - circle_x) * (x - circle_x) + 
            (y - circle_y) * (y - circle_y) <= rad * rad):
            return True
        else:
            return False

    # moveZone fixed x and y
    # attackingzone and followingzone x = enemy.rect.x , same for y

    def inAttack_Range(self):
        player = self.handler.game.gameState.player
        enemy = self.handler.game.gameState.enemy
        if utils.isInside(enemy.x , enemy.y, enemy.attack_rad, player.character.rect.x, player.character.rect.y):
            return True
        return False

    def enemy_move(self):

        if self.character.collided:

            if self.enemy_collision_side == 'right' :
                self.character.moveRight = False

            if self.enemy_collision_side == 'left' :
                self.character.moveLeft = False

            if self.enemy_collision_side == 'top' :
                self.character.moveUp = False

            if self.enemy_collision_side == 'bottom' :
                self.character.moveDown = False

    # def enemyMoveState(self, enemy, player_pos):
    #     if player_pos not in enemy.moveZone:
    #         if player in enemy.followingZone:
    #             if player_pos in attackingZone:
    #                 enemy.attack()
    #             else : enemy.follow()
    #         else : enemy.move


    # def inAttackRange():
	# 	if utils.isInside(eAttackRange.getCenterX(), eAttackRange.getCenterY(),eAttackRange.getWidth()/2, 
	# 			handler.getGame().gameState.getPlayer().getActualX(), handler.getGame().gameState.getPlayer().getActualY()))
	# 		return true;
	# 	return false;

    # def check_collision(self, sprite, group):
    #     return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def tick(self):
        self.character.tick()
        # self.handler.characterManager.check_rect_collision(self.character.rect, self.handler.characterManager.collided_entity(self.character))
        # self.enemy_move()
        self.behave()
        

    def draw(self):
        self.character.draw()