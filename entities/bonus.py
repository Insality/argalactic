# coding: utf-8
__author__ = 'Insality'

from entities.entity import Entity
import config
import profile
import random
import cocos
from cocos.actions import *

BONUS_CRYSTAL = 'res/crystal.png'
BONUS_SPEED = 'res/speed_bonus.png'

bonuses = [BONUS_CRYSTAL, BONUS_SPEED]

class Bonus(Entity):
    def __init__(self, type, pos):
        super(Bonus, self).__init__(type)
        self.type = type
        self.position = pos
        self.speed_x = random.choice([-2,-1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
        self.speed_y = random.choice([-3, -2,-1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
        self.max_speed = random.choice([6, 6.5, 7])
        self.crystal_count = random.randint(5, 10)

        self.bonus_back = cocos.sprite.Sprite('res/bonus_back.png')
        self.bonus_back.do(cocos.actions.Repeat(cocos.actions.RotateBy(360, 1)))
        self.add(self.bonus_back)

        self.schedule(self.update)

    @staticmethod
    def spawn(target, type, pos):
        target.add(Bonus(type, pos))

    def update(self, dt):
        if (self.is_far_outside()):
            self.destroy()

        if (self.speed_y < self.max_speed):
            self.speed_y += 0.1

        if (self.speed_x > 0.1):
            self.speed_x -= 0.05
        elif (self.speed_x < -0.1):
            self.speed_x +=0.05
        else:
            self.speed_x = 0

        self.x -= self.speed_x
        self.y -= self.speed_y

    def collide(self, other):
        if other.type == config.ENTITY_PLAYER:
            if self.type == BONUS_CRYSTAL:
                profile.profile['crystals'] += self.crystal_count
                self.destroy()
            if self.type == BONUS_SPEED:
                profile.BONUS_SPEED_TIME += 5
                self.destroy()

    def destroy(self):
        self.kill()
