# coding: utf-8
__author__ = 'Insality'

from entities.entity import Entity
import config
from cocos.actions import Repeat, RotateBy
import math
bullet_image = {
    config.ENTITY_ENEMY_BULLET: "enemy_bullet.png",
    config.ENTITY_FROGBOSS_BULLET: "boss1_bullet.png",
    config.ENTITY_PLAYER_BULLET: "bullet.png"
}

class Bullet(Entity):
    def __init__(self, pos, type):
        super(Bullet, self).__init__(bullet_image[type])
        self.type = type
        self.position = pos
        self.speed = 9
        self.damage = 1
        self.schedule(self.update_out_screen)

    def update_out_screen(self, dt):
        if (self.is_outside()):
            self.destroy()

    def destroy(self):
        self.kill()

class PlayerBullet(Bullet):
    def __init__(self, pos):
        super(PlayerBullet, self).__init__(pos, config.ENTITY_PLAYER_BULLET)
        self.type = config.ENTITY_PLAYER_BULLET
        self.position = pos
        self.speed = 9
        self.damage = 1
        self.schedule(self.move)

    def move(self, dt):
        self.y += self.speed

class EnemyBullet(Bullet):
    def __init__(self, pos, direction = 180):
        super(EnemyBullet, self).__init__(pos, config.ENTITY_ENEMY_BULLET)
        self.type = config.ENTITY_ENEMY_BULLET
        self.position = pos
        self.move_speed = 6
        self.damage = 2
        self.schedule(self.move)
        self.direction = direction
        self.do(Repeat( RotateBy (360, 1)))

    def move(self, dt):
        self.move_by_direction()
