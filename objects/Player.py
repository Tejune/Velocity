import pygame as pg
import random

class Player ():

    def __init__(self, engine, size=(100, 100), position=(0, 0), color=(255, 255, 255)):
        #Setup base properties
        self.WIN = engine.WIN
        self.size_x = size[0]
        self.size_y = size[1]
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.color = color

        #get services
        self.TS = engine.getService("TweenService")
        self.TweenStyle = "exponential"
        self.Speed = 5

    def __getitem__ (self, key):
        return getattr(self, key)
    
    def __setitem__ (self, key, newvalue):
        return setattr(self, key, newvalue)

    def eventStep (self, engine, events, dt):

        self.TweenTime = (dt / 1000) * 5
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.TS.create(self, self.TweenStyle, self.TweenTime, {"pos_y": self.pos_y - self.Speed}).play()
        elif keys[pg.K_a]:
            self.TS.create(self, self.TweenStyle, self.TweenTime, {"pos_x": self.pos_x - self.Speed}).play()
        elif keys[pg.K_s]:
            self.TS.create(self, self.TweenStyle, self.TweenTime, {"pos_y": self.pos_y + self.Speed}).play()
        elif keys[pg.K_d]:
            self.TS.create(self, self.TweenStyle, self.TweenTime, {"pos_x": self.pos_x + self.Speed}).play()


    def draw (self, engine):
        #Draw to screen
        pg.draw.rect(self.WIN, self.color, (self.pos_x, self.pos_y, self.size_x, self.size_y))
