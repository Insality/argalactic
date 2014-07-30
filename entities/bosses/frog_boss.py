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
        self.max_hp = 60
        self.hp = self.max_hp
        self.rotation = 180


        self.turrets = []
        self.turrets.append(FrogBossTurret((-87, 61)))
        self.add(self.turrets[0])
        self.turrets.append(FrogBossTurret((-55, 53)))
        self.add(self.turrets[1])
        self.turrets.append(FrogBossTurret((47, 53)))
        self.add(self.turrets[2])
        self.turrets.append(FrogBossTurret((89, 61)))
        self.add(self.turrets[3])
        self.last_turret = 0

        self.state = 1
        self.do(MoveTo((config.GAME_WIDTH/2, config.GAME_HEIGHT - 150), 1))
        self.schedule_interval(self.shoot, 0.2)
        self.schedule(self.update_state)

    def move(self):
        pass
    
    def shoot(self, dt):
        self.turrets[self.last_turret].shoot()
        self.last_turret += 1
        self.last_turret %= len(self.turrets)
        self.unschedule(self.shoot)
        self.schedule_interval(self.shoot, 0.2/self.state)

    def update_state(self, dt):
        if (float(self.hp)/self.max_hp < 0.3 and self.state == 1):
            self.state = 3

    def after_start(self):
        action = CallFunc(self.parent.parent.background_layer.set_speed, 0)
        action += Delay(1)
        action += CallFunc(self.parent.parent.background_layer.set_speed, -3)
        self.do(action)

    def before_destroy(self):
        self.parent.parent.background_layer.set_speed(3)
        self.parent.parent.add(cocos.text.Label('GAME COMPLETE!', font_size=32, x=config.GAME_WIDTH/2,
                                          y=config.GAME_HEIGHT/2 + 128, bold=True, anchor_x='center', anchor_y='center'))
        self.parent.parent.add(cocos.text.Label('Press ESC', font_size=24, x=config.GAME_WIDTH/2,
                                          y=config.GAME_HEIGHT/2, anchor_x='center', anchor_y='center'))

    def reward(self):
        self.parent.do( ( CallFuncS(Bonus.spawn, BONUS_CRYSTAL, self.position) + Delay(0.07) )*15)


class FrogBossTurret(Entity):
    def __init__(self, pos):
        super(FrogBossTurret, self).__init__("res/boss1_turret.png")
        self.anchor_y = -25
        self.position = pos
        self.y -= self.anchor_y

        self.schedule(self.rotate)

    def rotate(self, dt):
        player_pos = self.parent.parent.player.position
        self.direction = self.angle_with(player_pos)
        self.rotation = self.parent.rotation + self.direction


    def get_shoot_pos(self):
        my_pos = self.get_position()
        return my_pos

    def shoot(self):
        self.parent.parent.add(FrogBossBullet(self.get_shoot_pos(), self.direction))

class FrogBossBullet(Bullet):
    def __init__(self, pos, direction):
        super(FrogBossBullet, self).__init__(pos, config.ENTITY_FROGBOSS_BULLET)
        self.type = config.ENTITY_ENEMY_BULLET
        self.move_speed = 5
        self.damage = 3
        self.position = pos
        self.direction = direction
        self.rotation = self.direction

        self.schedule(self.move)

    def move(self, dt):
        self.move_by_direction()

