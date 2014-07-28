# coding: utf-8
__author__ = 'Insality'

from entities.bullet import *
from entities.bonus import *
import config
import profile
from random import randint, random

class Enemy(Entity):
    def __init__(self, pos, img):
        super(Enemy, self).__init__(img)
        self.type = config.ENTITY_ENEMY
        self.position = pos

        self.score_value = 50
        self.max_hp = 1
        self.hp = self.max_hp
        self.move_speed = 5

        self.schedule(self.update)

    def update(self, dt):
        self.x -= self.move_speed

        if (self.is_far_outside()):
            self.kill()

    def collide(self, other):
        if other.type == config.ENTITY_PLAYER_BULLET:
            self.damage(other.damage)
            other.destroy()

    def damage(self, value):
        self.hp -= value
        if self.hp<=0:
            self.destroy()

    def destroy(self):
        profile.profile['score'] += self.score_value
        self.reward()
        self.kill()

    def reward(self):
        if (random()*100 < 20):
            self.parent.do((SpawnBonus(BONUS_CRYSTAL, self.position) + Delay(0.1))*2)

class SimpleEnemy(Enemy):
    def __init__(self, pos):
        super(SimpleEnemy, self).__init__(pos, "res/simple_enemy.png")
        self.score_value = 50

class ShootEnemy(Enemy):
    def __init__(self, pos):
        super(ShootEnemy, self).__init__(pos, "res/shooter_enemy.png")
        self.score_value = 125
        self.move_speed = 3
        self.shoot_speed = 2
        self.max_hp = 2
        self.hp = self.max_hp
        self.schedule_interval(self.shoot, self.shoot_speed)

    def shoot(self, dt):
        self.parent.add(EnemyBullet(self.x-18, self.y))

    def reward(self):
        if (random()*100 < 20):
            self.parent.do((SpawnBonus(BONUS_CRYSTAL, self.position) + Delay(0.1))*3)