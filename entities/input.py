# coding: utf-8
__author__ = 'Insality'

import cocos
class Input(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super( Input, self ).__init__()
        self.buttons = set()

    def on_key_press(self, key, modifiers):
        self.buttons.add(key)

    def on_key_release(self, key, modifiers):
        try:
            self.buttons.remove(key)
        except KeyError:
            pass
