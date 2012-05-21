import pygame

class MenuEntry:
    """ Represents an entry in the menu """
    
    def __init__(self, text, ratioInY):
        """ Sets the entry's text """
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.text = text
        self.yRatio = ratioInY
        
    def draw(self, window):
        """ Draws the menu entry on the window """
        text = self.font.render(self.text, 1, (10, 10, 10))
        textpos = text.get_rect(centerx = window.get_width()/2, centery= window.get_height()/self.yRatio)
        window.blit(text, textpos)
        
    def setBold(self, bold):
        """ Sets the Boldness of the entry """
        self.font.set_bold(bold)