import pygame
from pygame.locals import *

from Screen.GUI.view import View
from Screen.GUI.pygame_helper import load_image
from menu_entry_view import MenuEntryView

class MenuView(View):
    """ Represents the menu on the main menu screen """
    
    def __init__(self, menu):
        """ Build the menu """
        self.entries = []
        for i in range(len(menu.entries)):
            entryView = MenuEntryView(menu.entries[i], 4.0/(i+1))
            self.entries.append(entryView)
        
        self.image = load_image("menu.png")
        
    def draw(self): 
        """ Draw the menu """
        menuSurface = self.getMenu()
        self.drawEntries(menuSurface)
        return menuSurface
        
    def drawEntries(self, menuSurf):
        """ Draws the menu entries on the Menu Surface """
        for entry in self.entries:
            entrySurface = entry.draw()
            yRatio = (self.entries.index(entry) + 1)/4.0
            entryPos = entrySurface.get_rect(centerx = menuSurf.get_width()/2, centery= menuSurf.get_height()*yRatio)
            menuSurf.blit(entrySurface, entryPos)
        
    def getMenu(self):
        """ Build the Surface for the menu """
        return load_image("menu.png")