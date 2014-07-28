# coding: utf-8
__author__ = 'Insality'

from entities.entity import Entity
import config
import profile
import random
import cocos
from cocos.actions import *

BONUS_CRYSTAL = 'res/crystal.png'


class SpawnBonus(InstantAction):
    def __init__(self, type, pos):
        super(SpawnBonus, self).__init__()
        self.type = type
        self.pos = pos

    def start(self):
        self.target.add(Bonus(self.pos, self.type))

class Bonus(Entity):
    def __init__(self, pos, type):
        super(Bonus, self).__init__(type)
        self.type = type
        self.position = pos
        self.speed_x = random.choice([0, 1, 1.5, 2, 2.5, 3])
        self.speed_y = random.choice([-2,-1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
        self.max_speed = random.choice([6, 6.5, 7])
        self.crystal_count = random.randint(5, 10)

        self.bonus_back = cocos.sprite.Sprite('res/bonus_back.png')
        self.bonus_back.do(cocos.actions.Repeat(cocos.actions.RotateBy(360, 1)))
        self.add(self.bonus_back)

        self.schedule(self.update)


    def update(self, dt):
        if (self.is_far_outside()):
            self.destroy()

        if (self.speed_x < self.max_speed):
            self.speed_x += 0.1

        if (self.speed_y > 0.1):
            self.speed_y -= 0.05
        elif (self.speed_y < -0.1):
            self.speed_y +=0.05
        else:
            self.speed_y = 0

        self.x -= self.speed_x
        self.y -= self.speed_y

    def collide(self, other):
        if other.type == config.ENTITY_PLAYER:
            profile.profile['crystals'] += self.crystal_count
            self.destroy()

    def destroy(self):
        self.kill()
