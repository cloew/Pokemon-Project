import pygame

class MessageBox:
    """ Represents a message box on the screen """
    
    def __init__(self, message):
        """ Builds the Message Box with the given message box """
        self.message = message
        self.charsShown = 0
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.stringToDisplay = ""
    
    def update(self):
        """ Updates the message box """
        if self.charsShown < self.message.length():
            self.charsShown += 1
            
        self.stringToDisplay = self.message.getMessageSlice(self.charsShown)
        
    def draw(self, window):
        """ Draws the message box on the window """
        surface = self.getBackgroundSurface()
        text = self.font.render(self.stringToDisplay, 1, (10, 10, 10))
        surface.blit(text, (0,0))
        surface.blit(text, (0, 42))
        return surface
        
    def getBackgroundSurface(self):
        """ Returns the background surface """
        surface = pygame.Surface((576, 82))
        surface.set_colorkey((0, 0, 0))
        surface.fill((0, 0, 0))
        return surface