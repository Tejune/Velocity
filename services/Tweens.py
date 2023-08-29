#TweenService
#Handles animations of objects and values

import math

def linear (a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b
def exponential (a: float, b: float, t: float) -> float:
    new_t = 0
    if t == 0:
        new_t = 0
    elif t == 1:
        new_t = 1
    elif t < 0.5:
        new_t = math.pow(2, 20 * t - 10) / 2
    else:
        new_t = (2 - math.pow(2, -20 * t + 10)) / 2
    return linear(a, b, new_t)

def clamp (num, minVal, maxVal):
    return max(min(num, maxVal), minVal)

INTERPOLATION_STYLES = {
    "linear": linear,
    "exponential": exponential
}

class Tween:
    def __init__ (self, tweenService, object, tweenType, time, properties):
        self.TWEEN_SERVICE = tweenService
        self.isPlaying = False
        self.t = 0.0
        self.time = time
        self.object = object
        self.tweenType = tweenType
        self.properties = properties
        self.startProperties = {}
    
        #get starting values
        for indx, _ in properties.items():
            self.startProperties[indx] = self.object[indx]   

    def play (self):
        self.isPlaying = True

    def stop (self):
        self.isPlaying = False

    def remove (self):
        #Remove tween from storage
        self.TWEEN_SERVICE.createdTweens.remove(self)

class TweenService:
    def __init__ (self):
        #create tween storage array
        self.createdTweens = []

    def create (self, object, tweenType: str, time: float | int, properties: {}) -> Tween:
        newTween = Tween(self, object, tweenType, time, properties)
        self.createdTweens.append(newTween)
        return newTween
    
    def onRender (self, deltaTime):
        #update tweens and their attached objects
        for tween in self.createdTweens:
            tween.t = clamp(tween.t + (deltaTime / 1000) / tween.time, 0, 1)

            #update objects
            for indx, origValue in tween.startProperties.items():
                result = INTERPOLATION_STYLES[tween.tweenType](origValue, tween.properties[indx], tween.t)
                tween.object[indx] = result

            #if reached end of tween, remove it
            if tween.t == 1:
                tween.remove()