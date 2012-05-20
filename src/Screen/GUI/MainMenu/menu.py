import pygame

from Screen.GUI.pygame_helper import load_image
from menu_entry import MenuEntry

class Menu:
    """ Represents the menu on the main menu screen """
    
    def __init__(self):
        """ Build the menu """
        self.entry = MenuEntry("Start Game")
        self.menuSurface = load_image("menu.png")#pygame.Surface((200, 200))
        
    def draw(self, window): 
        """ Draw the menu """
        menuSurface, menuPos = self.getMenu(window)
        self.entry.draw(menuSurface)
        window.blit(menuSurface, menuPos)
        
    def getMenu(self, window):
        """ Build the Surface for the menu """
        menuSurface = load_image("menu.png")
        
        x = window.get_width()/2
        y = 11*window.get_height()/16
        
        menuPos = menuSurface.get_rect(centerx = x, centery= y)
        return menuSurface, menuPos
        
    def setBold(self, bold):
        """ Set the boldness of the font """
        self.entry.setBold(bold)