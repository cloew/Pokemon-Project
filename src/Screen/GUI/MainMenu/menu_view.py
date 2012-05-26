import pygame
from pygame.locals import *

from Screen.GUI.pygame_helper import load_image
from menu_entry import MenuEntry

class MenuView:
    """ Represents the menu on the main menu screen """
    
    def __init__(self, menu):
        """ Build the menu """
        self.entries = [MenuEntry("Start", 4), MenuEntry("Exit", 2)]
        self.image = load_image("menu.png")
        self.selected = 0
        self.getEntry().setBold(True)
        
    def draw(self, window): 
        """ Draw the menu """
        menuSurface, menuPos = self.getMenu(window)
        for entry in self.entries:
            entry.draw(menuSurface)
        window.blit(menuSurface, menuPos)
        
    def getMenu(self, window):
        """ Build the Surface for the menu """
        menuSurface = load_image("menu.png")
        
        x = window.get_width()/2
        y = 11*window.get_height()/16
        
        menuPos = menuSurface.get_rect(centerx = x, centery= y)
        return menuSurface, menuPos
        
    def up(self):
        """ Move the selected index up """
        if self.selected > 0:
            self.changeHighlighted(-1)
        
    def down(self):
        """ Move the selected index down """
        if self.selected < len(self.entries)-1:
            self.changeHighlighted(1)
            
    def changeHighlighted(self, mod):
        """ Change the highlighted menu entry """
        self.getEntry().setBold(False)
        self.selected += mod
        self.getEntry().setBold(True)
        
    def getEntry(self):
        return self.entries[self.selected]