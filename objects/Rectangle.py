import pygame as pg
import random
from objects.Object import *

class Rectangle (Object):

    def __init__(self, engine, size=(100, 100), position=(0, 0), color=(255, 255, 255)):
        #Setup base properties
        self.WIN = engine.WIN
        self.size_x = size[0]
        self.size_y = size[1]
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.color = color

        self.dtc = 0

    def __getitem__ (self, key):
        return getattr(self, key)
    
    def __setitem__ (self, key, newvalue):
        return setattr(self, key, newvalue)

    def eventStep (self, engine, events, dt):
        self.dtc += dt
        if self.dtc >= 500:
               self.dtc = 0
               engine.getService("TweenService").create(self, "exponential", 0.4, {"pos_x": random.randint(-100, 1000), "pos_y": random.randint(-100, 450)}).play()
               engine.getService("TweenService").create(self, "exponential", 0.4, {"size_x": random.randint(0, 1000), "size_y": random.randint(0, 450)}).play()

    def draw (self, engine):
        #Draw to screen
        pg.draw.rect(self.WIN, self.color, (self.pos_x, self.pos_y, self.size_x, self.size_y))
