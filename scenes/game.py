# coding: utf-8
__author__ = 'Insality'

import cocos
import entities.player
from entities.input import Input
import entities.enemy
import cocos.collision_model as cm
import config
import profile
from entities.enemy_manager import EnemyManager
from cocos.actions import *
import random
from pyglet.window import key
import soundex

class Game(cocos.scene.Scene):
    def __init__(self):
        super(Game, self).__init__()
        self.background_layer = self.get_background_layer()
        self.add( self.background_layer, z=-1, name='background')

        self.add( Input(), z=0, name='input')

        self.game_layer = self.get_game_layer()
        self.add( self.game_layer, z=1, name='game_layer')

        self.enemy_manager = EnemyManager()
        self.add( self.enemy_manager, z = 1, name='enemy_manager')

        self.start_music()

        self.hud_layer = self.get_hud_layer()
        self.add( self.hud_layer, z=3, name='hud_layer')

    def get_background_layer(self):
        return BackgroundLayer()

    def get_game_layer(self):
        return GameLayer()

    def get_hud_layer(self):
        return HUDLayer()

    def start_music(self):
        self.music = soundex.load('music/theme1.mp3')
        soundex.music_volume(40)
        soundex.sound_volume(40)
        soundex.play_music()

class GameLayer(cocos.layer.Layer):
    def __init__(self):
        super(GameLayer, self).__init__()

        self.player = entities.player.Player()
        self.add(self.player)

        self.collman = cm.CollisionManagerGrid(0, config.GAME_WIDTH, 0, config.GAME_HEIGHT, 128, 128)
        self.schedule(self.update)
        self.schedule_interval(self.update_second, 1)

    def update(self, dt):
        self.collman.clear()
        for actor in self.get_children():
            self.collman.add(actor)

        for first, other in self.collman.iter_all_collisions():
            first.collide(other)
            other.collide(first)

    def update_second(self, dt):
        self.update_bonuses()

    def update_bonuses(self):
        if profile.BONUS_SPEED_TIME > 0:
            profile.BONUS_SPEED_TIME -= 1
        if profile.BONUS_SHIELD_TIME > 0:
            profile.BONUS_SHIELD_TIME -= 1

class HUDLayer(cocos.layer.Layer):
    def __init__(self):
        super(HUDLayer, self).__init__()

        self.hud_score = profile.profile['score']
        self.score_label = cocos.text.Label('', font_size=18, x=0, y=config.GAME_HEIGHT, anchor_x='left', anchor_y='top')
        self.add(self.score_label)

        self.hud_crystal = profile.profile['crystals']
        self.crystal_label = cocos.text.Label('', font_size=18, x=0, y=config.GAME_HEIGHT - 32, anchor_x='left', anchor_y='top')
        self.add(self.crystal_label)

        self.schedule(self.update)

    def update(self, dt):
        self.score_label.element.text = 'Score: %i' % self.hud_score
        if (self.hud_score < profile.profile['score']):
            self.hud_score+=4
        else:
            self.hud_score = profile.profile['score']

        self.crystal_label.element.text = 'Crystals: %i' % self.hud_crystal
        if (self.hud_crystal < profile.profile['crystals']):
            self.hud_crystal+=1
        else:
            self.hud_crystal = profile.profile['crystals']

class BackgroundLayer(cocos.layer.Layer):
    def __init__(self):
        super(BackgroundLayer, self).__init__()
        self.speed = 1
        stars_count = 100
        for i in range(stars_count):
            self.add(BackgroundStar())

    def set_speed(self, value):
        self.goal_speed = value
        self.schedule(self.change_smooth_speed)

    def change_smooth_speed(self, dt):
        delta = 0.02
        if (self.goal_speed < self.speed):
            delta *= -1

        self.speed += delta

        if (abs(self.speed - self.goal_speed) < delta*5):
            self.speed = self.goal_speed
            self.unschedule(self.change_smooth_speed)

class BackgroundStar(cocos.sprite.Sprite):
    def __init__(self):
        super(BackgroundStar, self).__init__("star.png")
        self.speed = random.randint(8, 40)/10.
        self.scale = random.randint(1, 7)/10.
        bright = random.randint(0, 125)+124

        self.color= (bright, bright, bright)
        self.w,self.h = cocos.director.director.get_window_size()
        self.position = (random.randint(0, self.w), random.randint(0, self.h))
        self.schedule(self.update)

    def update(self, dt):
        self.y -= self.speed * self.parent.speed
        if (self.y <= -30):
            self.position = (random.randint(0, self.w), self.h+10 )
        if (self.y >= config.GAME_HEIGHT + 30):
            self.position = (random.randint(0, self.w), -10 )