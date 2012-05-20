import random
import pygame

from pygame.locals import *
from Screen.GUI.pygame_helper import load_image

class ScrollingMap:
    """ Represents the scrolling map """
    
    def __init__(self):
        """ Builds the scrolling map and starts it at the top left corner  """
        self.image = load_image("pokearth.png")
        self.mapLoc = [0, 0]
        self.coord = [0, 0]
        
        self.xRange = range(1100-640)
        self.yRange = range(850-480)
    
    def draw(self, window):
        """ Draws the portion of the map from the mapLocation as the top left corner """
        x, y = int(self.mapLoc[0]), int(self.mapLoc[1])
        rect = Rect(x, y, 640, 480)
        imgPiece = self.image.subsurface(rect)
        window.blit(imgPiece, (0, 0))
        
    def update(self):
        """ Updates the map Location """
        if self.coord == self.mapLoc:
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
        
        denom = self.getDenominator(diff)
        self.mapLoc[0] += diff[0]/denom
        self.mapLoc[1] += diff[1]/denom
    
    def getDenominator(self, diff):
        """ Gets the determinator """
        if diff[0] == 0 or diff[1] == 0:
            denom = 1
        elif diff[0] > diff[1]:
            denom = float(abs(diff[0]))
        else:
            denom = float(abs(diff[1]))
        return denom