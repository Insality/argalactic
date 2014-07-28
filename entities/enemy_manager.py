# coding: utf-8
from entities.bosses.frog_boss import FrogBoss

__author__ = 'Insality'

from entities.enemy import *
import config
from cocos.actions import *

enemies = [SimpleEnemy, ShootEnemy]
spawn_zone = []
spawn_zone_count = 8

class EnemyManager(cocos.layer.Layer):
    def __init__(self):
        super(EnemyManager, self).__init__()
        delta_y = (config.GAME_HEIGHT - 32)/spawn_zone_count
        for i in range(spawn_zone_count):
            spawn_zone.append((config.GAME_WIDTH+256, delta_y * i + 32))

        self.schedule_interval(self.spawn_boss, 1)

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

class Spawn(InstantAction):
    def __init__(self, entity, pos):
        super(Spawn, self).__init__()
        self.entity = entity
        self.pos = pos

    def start(self):
        self.target.add(DangerArrow(config.GAME_WIDTH - 16, self.pos[1]))
        self.target.parent.game_layer.add(self.entity(self.pos))

class DangerArrow(Entity):
    def __init__(self, x, y):
        super(DangerArrow, self).__init__("res/arrow.png")
        self.position = x, y
        self.scale = 1.5
        self.do( (MoveBy((-16, 0), 0.3) + Reverse(MoveBy((-16, 0), 0.3))) * 3)
        self.schedule_interval(self.destoy, 1.2)

    def destoy(self, dt):
        self.kill()