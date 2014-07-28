# coding: utf-8
__author__ = 'Insality'

import cocos
import config
import cocos.collision_model as cm
import cocos.euclid as eu
import math

class Entity(cocos.sprite.Sprite):
    def __init__(self, img):
        super(Entity, self).__init__(img)
        self.type = config.ENTITY_UNDEFINED
        rx = self.image.width
        ry = self.image.height

        self.cshape = cm.AARectShape(eu.Vector2(0.0, 0.0), rx/2 * 0.8, ry/2 * 0.8)
        self.schedule(self.update_cshape)

    def is_outside(self):
        if (self.x < 0 or self.y < 0 or self.x > config.GAME_WIDTH or self.y > config.GAME_HEIGHT):
            return True

    def is_far_outside(self):
        if (self.x < -config.GAME_WIDTH or self.y < -config.GAME_HEIGHT or self.x > config.GAME_WIDTH*2 or self.y > config.GAME_HEIGHT*2):
            return True

    def update_cshape(self, dt):
        self.cshape.center = self.x, self.y

    def collide(self, other):
        pass

    def kill(self):
        if (self in self.parent.get_children()):
            cocos.sprite.Sprite.kill(self)

    def angle_between(self, pos1, pos2):
        deltaY = pos1[1] - pos2[1]
        deltaX = pos1[0] - pos2[0]
        return math.degrees(math.atan2(deltaY, deltaX))

    def angle_with(self, pos):
        deltaY = self.y - pos[1]
        deltaX = self.x - pos[0]
        return math.degrees(math.atan2(deltaY, deltaX))