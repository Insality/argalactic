# coding: utf-8
__author__ = 'Insality'

from entities.entity import Entity
import config
from cocos.actions import Repeat, RotateBy

bullet_image = {
    config.ENTITY_ENEMY_BULLET: "res/enemy_bullet.png",
    config.ENTITY_FROGBOSS_BULLET: "res/boss1_bullet.png",
    config.ENTITY_PLAYER_BULLET: "res/bullet.png"
}

class Bullet(Entity):
    def __init__(self, x, y, type):
        super(Bullet, self).__init__(bullet_image[type])
        self.type = type
        self.position = (x, y)
        self.speed = 9
        self.damage = 1
        self.schedule(self.update)

    def update(self, dt):
        if (self.is_outside()):
            self.destroy()

    def destroy(self):
        self.kill()

class PlayerBullet(Bullet):
    def __init__(self, x, y):
        super(PlayerBullet, self).__init__(x, y, config.ENTITY_PLAYER_BULLET)
        self.type = config.ENTITY_PLAYER_BULLET
        self.schedule(self.update)
        self.position = (x, y)
        self.speed = 9
        self.damage = 1
        self.schedule(self.move)

    def move(self, dt):
        self.x += self.speed

class EnemyBullet(Bullet):
    def __init__(self, x, y):
        super(EnemyBullet, self).__init__(x, y, config.ENTITY_ENEMY_BULLET)
        self.type = config.ENTITY_ENEMY_BULLET
        self.schedule(self.update)
        self.position = (x, y)
        self.speed = 6
        self.damage = 2
        self.schedule(self.move)
        self.do(Repeat( RotateBy (360, 1)))


    def move(self, dt):
        self.x -= self.speed
