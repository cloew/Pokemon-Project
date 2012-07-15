import math
import random

import pygame
from pygame.locals import *
from Screen.GUI.view import View
from Screen.GUI.pygame_helper import load_image

class ScrollingMap(View):
    """ Represents the scrolling map """
    VELOCITY = 1
    
    def __init__(self):
        """ Builds the scrolling map and starts it at the top left corner  """
        self.image = load_image("pokearth.png")
        self.mapLoc = [0, 0]
        self.coord = [0, 0]
        
        self.xRange = range(1100-640)
        self.yRange = range(850-480)
    
    def draw(self):
        """ Draws the portion of the map from the mapLocation as the top left corner """
        x, y = int(self.mapLoc[0]), int(self.mapLoc[1])
        rect = Rect(x, y, 640, 480)
        return self.image.subsurface(rect)
        
    def update(self):
        """ Updates the map Location """
        if self.atCoord():
            self.getNewLoc()
        else:
            self.drift()
        
    def getNewLoc(self):
        """ Returns the new location """
        self.coord[0] = random.choice(self.xRange)
        self.coord[1] = random.choice(self.yRange)
        
    def drift(self):
        """ Have the map location drift """
        diff = [0, 0]
        diff[0] = self.coord[0] - self.mapLoc[0]
        diff[1] = self.coord[1] - self.mapLoc[1]
        
        if self.willOvershoot(diff):
            self.mapLoc = list(self.coord)
        else:
            angle = self.getAngle(diff)
            self.mapLoc[0] += math.cos(angle)
            self.mapLoc[1] += math.sin(angle)
            
    def atCoord(self):
        """ Return if the map is at the coord """
        sameX = self.coord[0] == int(self.mapLoc[0])
        sameY = self.coord[1] == int(self.mapLoc[1])
        return sameX and sameY
        
    def willOvershoot(self, diff):
        """ Returns if by moving at the velocity of one the map will miss the coord """ 
        distance = diff[0]**2 + diff[1]**2
        return distance < 1
        
    def getAngle(self, diff):
        """ Gets the angle to the coord """
        return math.atan2(diff[1], diff[0])
        
map = ScrollingMap()
