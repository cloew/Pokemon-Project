from Screen.Pygame.Menu.menu_background_widget import MenuBackgroundWidget

from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.widgets.sized_widget import SizedWidget

import pygame

class MessageBox(SizedWidget):
    """ Represents a message box on the screen """
    maxChars = 35
    
    def __init__(self, width, height, message, fullyDisplay=False):
        """ Builds the Message Box with the given message box """
        SizedWidget.__init__(self, width, height)
        self.message = message
        self.charsShown = 0
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.stringToDisplay = ""
        
        self.background = MenuBackgroundWidget(self.width, self.height)
        
        if fullyDisplay:
            self.showFully()
    
    def update(self):
        """ Updates the message box """
        if not self.isFullyShown():
            self.charsShown += 1
            
        self.stringToDisplay = self.message.getMessageSlice(self.charsShown)
        
    def drawSurface(self):
        """ Draws the message box """
        self.drawOnSurface(self.background.draw(), left=0, top=0)
        
        line1 = self.font.render(self.stringToDisplay[:self.maxChars], 1, (10, 10, 10)) # Logic to split string to display may belong better in model
        line2 = self.font.render(self.stringToDisplay[self.maxChars:], 1, (10, 10, 10))
        
        self.drawOnSurface(line1, left=.05, centery=.33)
        self.drawOnSurface(line2, left=.05, centery=.66)
        
    def isFullyShown(self):
        """ Returns if the current message string is fully shown """
        return self.charsShown >= self.message.length()
        
    def showFully(self):
        """ Make the message display fully """
        self.charsShown = self.message.length()