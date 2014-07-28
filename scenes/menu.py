# coding: utf-8
__author__ = 'Insality'

import cocos
from cocos.director import director
import pyglet
import config
import game

class Menu(cocos.scene.Scene):
    def __init__(self):
        super( Menu, self ).__init__()
        self.add( self.get_background_layer(), z=-1, name='background')
        self.add( self.get_menu_layer(), z=1, name='menu_layer')

    def get_background_layer(self):
        return cocos.layer.ColorLayer(64, 64, 120, 60)

    def get_menu_layer(self):
        return MenuLayer()

class MenuLayer(cocos.menu.Menu):
    def __init__(self):
        super(MenuLayer, self).__init__(config.GAME_TITLE)

        self.menu_valign = cocos.menu.BOTTOM
        self.menu_halign = cocos.menu.RIGHT

        self.font_title['font_name'] = 'Footlight MT Light'
        self.font_title['font_size'] = 86
        self.font_title['color'] = (20,200,200,255)

        item_start = cocos.menu.MenuItem('New Game', self.on_start )
        item_fullscreen = cocos.menu.ToggleMenuItem('Fullscreen: ', self.toggle_fullscreen, False)
        item_music_mute = cocos.menu.ToggleMenuItem('Music mute: ', self.toggle_music, False)
        item_exit = cocos.menu.MenuItem('Quit', self.on_quit )
        items = [item_start, item_fullscreen, item_music_mute, item_exit]

        self.create_menu(items)

    def toggle_fullscreen(self, value):
        director.window.set_fullscreen(value)

    def toggle_music(self, value):
        print("Toggle music is not implemented yet")

    def on_start(self):
        director.push(game.Game())

    def on_quit( self ):
        pyglet.app.exit()