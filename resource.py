__author__ = 'Insality'

import pyglet

pyglet.resource.path = ["res/"]
pyglet.resource.reindex()

player = pyglet.resource.image('player.png')
star = pyglet.resource.image('star.png')
boss_bullet = pyglet.resource.image('boss1_bullet.png')