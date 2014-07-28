# coding: utf-8
__author__ = 'Insality'

from entities.bullet import *
from entities.enemy import Enemy
import config
from entities.bonus import *
from cocos.actions import *
import math

class FrogBoss(Enemy):
    def __init__(self, pos):
        super(FrogBoss, self).__init__(pos, "res/boss1.png")
        self.score_value = 3000
        self.move_speed = 3
        self.shoot_speed = 2
        self.max_hp = 250
        self.hp = self.max_hp

        self.turrets = []
        self.turrets.append(FrogBossTurret((-61, -87)))
        self.add(self.turrets[0])
        self.turrets.append(FrogBossTurret((-53, -55)))
        self.add(self.turrets[1])
        self.turrets.append(FrogBossTurret((-53, 47)))
        self.add(self.turrets[2])
        self.turrets.append(FrogBossTurret((-61, 89)))
        self.add(self.turrets[3])
        self.last_turret = 0

        self.do(MoveTo((config.GAME_WIDTH - 150, config.GAME_HEIGHT/2), 1))
        self.schedule_interval(self.shoot, 0.3)


    def update(self, dt):
        if (self.is_far_outside()):
            self.kill()

    def shoot(self, dt):
        print self.last_turret
        self.turrets[self.last_turret].shoot()
        self.last_turret += 1
        self.last_turret %= len(self.turrets)

    def reward(self):
        self.parent.do((SpawnBonus(BONUS_CRYSTAL, self.position) + Delay(0.07))*15)

class FrogBossTurret(Entity):
    def __init__(self, pos):
        super(FrogBossTurret, self).__init__("res/boss1_turret.png")
        self.anchor_x = 25
        self.position = pos
        self.x -= self.anchor_x

        self.schedule(self.rotate)

    def rotate(self, dt):
        self.my_x = self.parent.x + self.x
        self.my_y = self.parent.y + self.y
        player = self.parent.parent.player
        angle = self.angle_between((self.my_x, self.my_y), (player.x, player.y))
        self.rotation = 360-angle

    def shoot(self):
        self.parent.parent.add(FrogBossBullet(self.my_x, self.my_y, 360-self.rotation))

class FrogBossBullet(Bullet):
    def __init__(self, x, y, angle):
        super(FrogBossBullet, self).__init__(x, y, config.ENTITY_FROGBOSS_BULLET)
        self.type = config.ENTITY_ENEMY_BULLET
        self.speed = 9
        self.damage = 3
        self.position = (x, y)
        self.angle = angle
        self.rotation = 360 - self.angle
        self.xx = math.sin(math.radians(angle-90))
        self.yy = -math.cos(math.radians(angle-90))

        self.schedule(self.move)

    def move(self, dt):
        self.x += self.speed * self.xx
        self.y += self.speed * self.yy

