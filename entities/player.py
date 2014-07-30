# coding: utf-8
__author__ = 'Insality'

from pyglet.window import key
from cocos.director import director
import bullet
from entities.entity import Entity
import config
import profile

class Player(Entity):
    def __init__(self):
        super(Player, self).__init__("res/player.png")
        self.type = config.ENTITY_PLAYER
        self.buttons = None
        self.position = (config.GAME_WIDTH/2, 64)

        self.top_gun_offset = (-16, 24)
        self.down_gun_offset = (16, 24)
        ''' 0 - верхная пушкая, 1 - нижняя '''
        self.last_shooted_gun = 0

        self.move_speed = 7
        self.base_shoot_speed = 8
        self.shoot_speed = self.base_shoot_speed

        self.schedule(self.update)
        self.schedule_interval (self.fire, 1./self.shoot_speed)

    def update(self, dt):
        if (self.buttons == None):
            self.buttons = director.scene.get('input').buttons

        if (key.UP in self.buttons):
            self.move(0, self.move_speed)
        if (key.DOWN in self.buttons):
            self.move(0, -self.move_speed)
        if (key.LEFT in self.buttons):
            self.move(-self.move_speed, 0)
        if (key.RIGHT in self.buttons):
            self.move(self.move_speed, 0)

        if profile.BONUS_SPEED_TIME > 0:
            self.shoot_speed = 2*self.base_shoot_speed
        else:
            self.shoot_speed = self.base_shoot_speed

    def fire(self, dt):
        if self.last_shooted_gun == 0:
            self.parent.add(bullet.PlayerBullet(( self.x + self.top_gun_offset[0], self.y + self.top_gun_offset[1]) ))
            self.last_shooted_gun = 1
        else:
            self.parent.add(bullet.PlayerBullet( (self.x + self.down_gun_offset[0], self.y + self.down_gun_offset[1]) ))
            self.last_shooted_gun = 0

        self.unschedule(self.fire)
        self.schedule_interval (self.fire, 1./self.shoot_speed)

    def move(self, dx, dy):
        width, height = director.get_window_size()
        image_cx, image_cy = self.image_anchor
        nextPos = self.x + dx, self.y + dy

        if (nextPos[0] + image_cx < (width) and nextPos[1] + image_cy < height
            and nextPos[0] - image_cx > 0 and nextPos[1] - image_cy > 0):
            self.x, self.y = nextPos

    def collide(self, other):
        if other.type == config.ENTITY_ENEMY:
            other.damage(other.max_hp)
        if other.type == config.ENTITY_ENEMY_BULLET:
            other.destroy()
            profile.profile['score'] -= 100*other.damage