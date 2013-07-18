import pygame

class MenuEntryView:
    """ Represents an entry in the menu """
    
    def __init__(self, entry, fontSize=36):
        """ Sets the entry's text """
        self.font = pygame.font.SysFont("Times New Roman", fontSize)
        self.entry = entry
        
    def draw(self):
        """ Draws the menu entry """
        self.font.set_bold(self.entry.selected)
        text = self.font.render(self.entry.getText(), 1, (10, 10, 10))
        return text
        
    def setBold(self, bold):
        """ Sets the Boldness of the entry """
        self.font.set_bold(bold)