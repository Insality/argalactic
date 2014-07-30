# coding: utf-8
__author__ = 'Insality'

from distutils.core import setup
import py2exe

setup(
    windows=[{"script":"argalactic.py"}],
    options={"py2exe": {"includes":["cocos", "pyglet", "sip"]}}
)