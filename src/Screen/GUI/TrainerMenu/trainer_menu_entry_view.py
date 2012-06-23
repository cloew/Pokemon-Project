import pygame

class TrainerMenuEntryView:
    """ Represents an entry in the trainer menu """
    HEIGHT_RATIO = 10.0
    
    def __init__(self, entry, ratioInY):
        """ Sets the entry's text """
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.entry = entry
        self.yRatio = ratioInY
        
    def draw(self, window):
        """ Draws the menu entry on the window """
        self.font.set_bold(self.entry.selected)
        text = self.font.render(self.entry.getText(), 1, (10, 10, 10))
        height = window.get_height()/self.HEIGHT_RATIO
        textpos = text.get_rect(centerx = window.get_width()/2, centery= height*(self.yRatio+.5))
        window.blit(text, textpos)
        
    def setBold(self, bold):
        """ Sets the Boldness of the entry """
        self.font.set_bold(bold)