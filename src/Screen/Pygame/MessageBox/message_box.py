from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.widgets.sized_widget import SizedWidget

import pygame

class MessageBox(SizedWidget):
    """ Represents a message box on the screen """
    maxChars = 35
    
    def __init__(self, message):
        """ Builds the Message Box with the given message box """
        SizedWidget.__init__(self, 576, 82)
        self.message = message
        self.charsShown = 0
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.stringToDisplay = ""
    
    def update(self):
        """ Updates the message box """
        if not self.isFullyShown():
            self.charsShown += 1
            
        self.stringToDisplay = self.message.getMessageSlice(self.charsShown)
        
    def drawSurface(self):
        """ Draws the message box """
        line1 = self.font.render(self.stringToDisplay[:self.maxChars], 1, (10, 10, 10)) # Logic to split string to display may belong better in model
        line2 = self.font.render(self.stringToDisplay[self.maxChars:], 1, (10, 10, 10))
        
        self.drawOnSurface(line1, left=0, top=0)
        self.drawOnSurface(line2, left=0, top=42.0/self.height)
        
    def isFullyShown(self):
        """ Returns if the current message string is fully shown """
        return self.charsShown >= self.message.length()