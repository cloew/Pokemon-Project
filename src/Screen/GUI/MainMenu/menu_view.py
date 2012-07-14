import pygame
from pygame.locals import *

from Screen.GUI.pygame_helper import load_image
from menu_entry_view import MenuEntryView

class MenuView:
    """ Represents the menu on the main menu screen """
    
    def __init__(self, menu):
        """ Build the menu """
        self.entries = []
        for i in range(len(menu.entries)):
            entryView = MenuEntryView(menu.entries[i], 4.0/(i+1))
            self.entries.append(entryView)
        
        self.image = load_image("menu.png")
        
    def draw(self, window): 
        """ Draw the menu """
        menuSurface, menuPos = self.getMenu(window)
        for entry in self.entries:
            entry.draw(menuSurface)
        return menuSurface
        
    def getMenu(self, window):
        """ Build the Surface for the menu """
        menuSurface = load_image("menu.png")
        
        x = window.get_width()/2
        y = 11*window.get_height()/16
        
        menuPos = menuSurface.get_rect(centerx = x, centery= y)
        return menuSurface, menuPos