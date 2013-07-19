from Screen.GUI.view import View

import pygame

class MessageBox(View):
    """ Represents a message box on the screen """
    maxChars = 35
    
    def __init__(self, message):
        """ Builds the Message Box with the given message box """
        self.message = message
        self.charsShown = 0
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.stringToDisplay = ""
    
    def update(self):
        """ Updates the message box """
        if not self.isFullyShown():
            self.charsShown += 1
            
        self.stringToDisplay = self.message.getMessageSlice(self.charsShown)
        
    def draw(self):
        """ Draws the message box """
        surface = self.getBackgroundSurface()
        line1 = self.font.render(self.stringToDisplay[:self.maxChars], 1, (10, 10, 10)) # Logic to split string to display may belong better in model
        line2 = self.font.render(self.stringToDisplay[self.maxChars:], 1, (10, 10, 10))
        
        surface.blit(line1, (0,0))
        surface.blit(line2, (0, 42))
        return surface
        
    def getBackgroundSurface(self):
        """ Returns the background surface """
        surface = pygame.Surface((576, 82))
        surface.set_colorkey((0, 0, 0))
        surface.fill((0, 0, 0))
        return surface
        
    def isFullyShown(self):
        """ Returns if the current message string is fully shown """
        return self.charsShown >= self.message.length()