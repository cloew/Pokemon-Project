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
        text = self.font.render(self.stringToDisplay, 1, (10, 10, 10))
        textpos = text.get_rect(centerx = window.get_width()/2, centery= 3*window.get_height()/4)
        window.blit(text, textpos)