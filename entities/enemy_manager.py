# coding: utf-8
from entities.bosses.frog_boss import FrogBoss

__author__ = 'Insality'

from entities.enemy import *
import config
from cocos.actions import *
from random import choice

enemies = [SimpleEnemy, ShootEnemy]
spawn_zone = []
spawn_zone_count = 8

class EnemyManager(cocos.layer.Layer):
    def __init__(self):
        super(EnemyManager, self).__init__()

        # Creating spawn zones:
        delta_x = (config.GAME_WIDTH - 32)/spawn_zone_count
        for i in range(spawn_zone_count):
            spawn_zone.append((delta_x * i + 32, config.GAME_HEIGHT+256 ))

        self.levels = Level()
        print(dir(self.levels))
        # self.schedule_interval(self.spawn_random, 4)
        self.do(self.start_level1())

    def spawn_boss(self, dt):
        action = Spawn(FrogBoss, spawn_zone[4])
        self.do( action )
        self.unschedule(self.spawn_boss)

    def spawn_random(self, dt):
        action = Spawn(enemies[0], spawn_zone[0])
        action += Spawn(enemies[0], spawn_zone[7])
        action += Delay(0.4)
        action += Spawn(enemies[0], spawn_zone[1])
        action += Spawn(enemies[0], spawn_zone[6])
        action += Delay(0.4)
        action += Spawn(enemies[1], spawn_zone[2])
        action += Spawn(enemies[1], spawn_zone[5])
        action += Delay(0.4)
        action += Spawn(enemies[1], spawn_zone[3])
        action += Spawn(enemies[1], spawn_zone[4])
        action += Delay(0.4)
        self.do( action )

    def start_level1(self):
        level = Delay(1)
        for i in range(4):
            level += choice(self.levels.levels)
            level += Delay(5)
        level += Spawn(FrogBoss, spawn_zone[4])
        return level

class Spawn(InstantAction):
    def __init__(self, entity, pos):
        super(Spawn, self).__init__()
        self.entity = entity
        self.pos = pos

    def start(self):
        self.target.add(DangerArrow(self.pos[0], config.GAME_HEIGHT - 16))
        self.target.parent.game_layer.add(self.entity(self.pos))

class DangerArrow(Entity):
    def __init__(self, x, y):
        super(DangerArrow, self).__init__("arrow.png")
        self.position = x, y
        self.scale = 1.5
        self.do( (MoveBy((0, -16), 0.3) + Reverse(MoveBy((0, -16), 0.3))) * 3)
        self.schedule_interval(self.destoy, 1.2)

    def destoy(self, dt):
        self.kill()


class Level:
    def __init__(self):
        self.levels = []

        wave = Spawn(choice(enemies), spawn_zone[0])
        wave += Spawn(choice(enemies), spawn_zone[7])
        wave += Delay(0.5)
        wave += Spawn(choice(enemies), spawn_zone[1])
        wave += Spawn(choice(enemies), spawn_zone[6])
        wave += Delay(0.5)
        wave += Spawn(choice(enemies), spawn_zone[2])
        wave += Spawn(choice(enemies), spawn_zone[5])
        wave += Delay(0.5)
        wave += Spawn(choice(enemies), spawn_zone[3])
        wave += Spawn(choice(enemies), spawn_zone[4])
        wave += Delay(0.5)

        self.levels.append(wave)


        wave = Spawn(choice(enemies), spawn_zone[3])
        wave += Spawn(choice(enemies), spawn_zone[4])
        wave += Delay(0.5)
        wave += Spawn(choice(enemies), spawn_zone[2])
        wave += Spawn(choice(enemies), spawn_zone[5])
        wave += Delay(0.5)
        wave += Spawn(choice(enemies), spawn_zone[1])
        wave += Spawn(choice(enemies), spawn_zone[6])
        wave += Delay(0.5)
        wave += Spawn(choice(enemies), spawn_zone[0])
        wave += Spawn(choice(enemies), spawn_zone[7])
        wave += Delay(0.5)

        self.levels.append(wave)


        wave = Spawn(choice(enemies), spawn_zone[0])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[1])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[2])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[3])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[4])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[5])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[6])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[7])

        self.levels.append(wave)


        wave = Spawn(choice(enemies), spawn_zone[7])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[6])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[5])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[4])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[3])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[2])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[1])
        wave += Delay(0.3)
        wave += Spawn(choice(enemies), spawn_zone[0])

        self.levels.append(wave)

        wave = Spawn(choice(enemies), spawn_zone[0])
        wave += Delay(0.4)
        wave = Spawn(choice(enemies), spawn_zone[0])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[1])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[1])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[2])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[2])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[3])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[3])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[4])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[4])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[5])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[5])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[6])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[7])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[7])

        self.levels.append(wave)

        wave = Spawn(choice(enemies), spawn_zone[3])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[4])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[3])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[4])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[3])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[4])
        wave += Delay(0.4)
        wave += Spawn(choice(enemies), spawn_zone[3])
        wave += Delay(0.4)

        self.levels.append(wave)