import pygame

class Menu:
    """ Represents the menu on the main menu screen """
    
    def __init__(self):
        """ Build the menu """
        self.font = pygame.font.SysFont("Times New Roman", 36)
        
    def draw(self, window): 
        """ Draw the menu """
        text = self.font.render("Start Game", 1, (10, 10, 10))
        textpos = text.get_rect(centerx = window.get_width()/2, centery= window.get_height()/2)
        window.blit(text, textpos)
        
    def setBold(self, bold):
        """ Set the boldness of the font """
        self.font.set_bold(bold)