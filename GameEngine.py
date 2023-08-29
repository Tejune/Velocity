#   Velocity Game Engine
#   By @Tejune

import pygame as pg
import sys

from objects.Rectangle import *
from objects.Player import *
from services.Tweens import *

class GameEngine:
    def __init__ (self, winSize=(1200, 650)):
        #initialize pygame
        pg.init()
        #set window size
        self.WIN_SIZE = winSize
        #get window object and set screen caption
        self.WIN = pg.display.set_mode(self.WIN_SIZE, pg.DOUBLEBUF)
        pg.display.set_caption("Velocity Engine")
        #create clock object to keep track of time
        self.clock = pg.time.Clock()

        #load services
        self.service = {}
        self.service["TweenService"] = TweenService()

        #create objects array
        self.objects = []

    def getService (self, service: str):
        return self.service[service]
    
    def checkEvents (self, dt):
        events = pg.event.get()

        #fire event method for each object
        for object in self.objects:
            object.eventStep(self, events, dt)

        #process exit events
        for event in events:
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def render (self, dt):
        #fire service onRender event
        for _, service in self.service.items():
            service.onRender(dt)

        #fill screen with black
        self.WIN.fill((10, 10, 20))
        #render every object in the array
        for object in self.objects:
            object.draw(self)
        #swap buffer
        pg.display.update()

    def run (self):
        while True:
            dt = self.clock.tick(60)
            self.checkEvents(dt)
            self.render(dt)
            self.clock.tick(60)

#Create and run engine object
if __name__ == "__main__":
    engine = GameEngine()
    #Add rectangle
    engine.objects.append(Rectangle(engine, size=(100, 100), position=(200, 200), color=(255, 0, 255)))
    engine.objects.append(Rectangle(engine, size=(100, 100), position=(200, 200), color=(0, 255, 255)))
    engine.objects.append(Rectangle(engine, size=(100, 100), position=(200, 200), color=(255, 255, 0)))

    #for i in range(255):
    #    engine.objects.append(Rectangle(engine, size=(1200, 659), position=(0, 0), color=(i, i, i)))

    #Start engine
    engine.run()
