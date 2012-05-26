import sys
sys.path.append("C:\\cygwin\\home\\Programming\\Pokemon-Python\\src")

import pygame
from pygame.locals import *
from Screen.GUI.pygame_helper import load_image

class Screen:
    """ Represents the screen """
    GAME_SPEED = 60
    
    def __init__(self):
        """ Build the window """
        self.window = self.getWindow()
        self.clock = pygame.time.Clock()
        
    def setScreen(self, screen):
        """ Sets the current Screen Display """
        self.screen = screen
        
    def getWindow(self):
        """ Gets the GUI Window """
        pygame.init()
        pygame.display.set_icon(self.getIcon())
        pygame.display.set_caption('Pokemon')
        pygame.mouse.set_visible(0)
        return pygame.display.set_mode((640, 480))
        
    def getIcon(self):
        """ Gets the icon """
        image = load_image("pokeball.png")
        return image
        
    def update(self):
        """ Update the screen """
        self.screen.update()
        
    def draw(self):
        """ Draws the screen """
        self.screen.draw(self.window)
        self.redraw()
        
    def run(self):
        """ Run the screen """
        self.running = True
        while self.running:
            self.clock.tick(self.GAME_SPEED)
            
            self.screen.update()
            self.processEvents()
            self.screen.draw(self.window)
            self.redraw()
            
    def redraw(self):
        pygame.display.flip()
        
if __name__ == "__main__":
    screen = Screen()
    screen.run()