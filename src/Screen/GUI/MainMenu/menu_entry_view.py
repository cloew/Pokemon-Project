import pygame

class MenuEntryView:
    """ Represents an entry in the menu """
    
    def __init__(self, entry, ratioInY):
        """ Sets the entry's text """
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.entry = entry
        self.yRatio = ratioInY
        
    def draw(self, window):
        """ Draws the menu entry on the window """
        self.font.set_bold(self.entry.selected)
        text = self.font.render(self.entry.text, 1, (10, 10, 10))
        textpos = text.get_rect(centerx = window.get_width()/2, centery= window.get_height()/self.yRatio)
        window.blit(text, textpos)
        
    def setBold(self, bold):
        """ Sets the Boldness of the entry """
        self.font.set_bold(bold)