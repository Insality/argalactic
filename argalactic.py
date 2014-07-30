# coding: utf-8
__author__ = 'Insality'

from scenes.menu import *
import pyglet
import config

def main():
    print("Hello, Argalactic!")
    director.init(resizable=True, caption=config.GAME_TITLE, width=config.GAME_WIDTH, height=config.GAME_HEIGHT)
    director.window.set_icon(pyglet.image.load('res/icon.png'))
    director.window.set_location(300, 0)
    menu_scene = Menu()

    director.run (menu_scene)

if __name__ == '__main__':
    main()