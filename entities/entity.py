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
        self.x, self.y = 1000, 1000
        self.scr_x, self.scr_y = self.x, self.y
        self.move_speed = 0
        # direction - move angle, rotation - image angle
        self.direction = 0

        rx = self.image.width
        ry = self.image.height
        self.cshape = cm.AARectShape( (self.x, self.y), rx/2 * 0.8, ry/2 * 0.8)

        self.schedule(self.update_sys)
        self.schedule_interval(self._after_start_schedule, 0.01)
        self._cached_direction = 0
        self._cached_speed = 0

    def move_by_direction(self, direction=None, speed=None):
        if (direction == None):
            direction = self.direction
        if (speed == None):
            speed = self.move_speed

        # input vars cached to opt. processing
        if (not (self._cached_direction == direction and self._cached_speed == speed) ):
            self._cached_direction = direction
            self._cached_speed = speed
            self.xx = math.sin(math.radians(direction))
            self.yy = math.cos(math.radians(direction))
        self.x += speed * self.xx
        self.y += speed * self.yy

    def _after_start_schedule(self, dt):
        self.after_start()
        self.unschedule(self._after_start_schedule)

    def after_start(self):
        pass

    def before_destroy(self):
        pass

    def update_sys(self, dt):
        self.update_cshape()
        self.update_screen_pos()

    # Needed for collisions
    def update_cshape(self):
        self.cshape.center = self.get_position()

    # my_x/y - screen coordinates
    def update_screen_pos(self):
        self.scr_x = self.get_world_transform()[6] - self.anchor_x
        self.scr_y = self.get_world_transform()[7] - self.anchor_y

    def get_position(self):
        return (self.scr_x, self.scr_y)

    def is_outside(self):
        if (self.x < 0 or self.y < 0
            or self.x > config.GAME_WIDTH or self.y > config.GAME_HEIGHT):
            return True

    def is_far_outside(self):
        if (self.x < -config.GAME_WIDTH or self.y < -config.GAME_HEIGHT
            or self.x > config.GAME_WIDTH*2 or self.y > config.GAME_HEIGHT*2):
            return True

    def collide(self, other):
        '''
        calling, when collide with other object. Should to override
        '''
        pass

    def kill(self):
        self.before_destroy()
        if (self in self.parent.get_children()):
            cocos.sprite.Sprite.kill(self)

    def angle_with(self, pos):
        '''
        :param pos: other point
        :return: direction with point pos. 0 - top, 90 - right, 180 - bottom, 270 - left
        '''
        my_pos = self.get_position()
        deltaY = my_pos[1] - pos[1]
        deltaX = my_pos[0] - pos[0]
        return 270 + (math.degrees(math.atan2(deltaY, deltaX)) * -1)