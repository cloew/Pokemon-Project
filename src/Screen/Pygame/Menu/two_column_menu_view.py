from Screen.Pygame.pygame_helper import GetTransparentSurface
from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

import pygame

class TwoColumnMenuView:
    """ Represents a Two Column Menu View """
    
    def __init__(self, menu):
        """ Initialize the Two Column Menu View """
        self.menu = menu
        self.font = pygame.font.SysFont("Times New Roman", 36)
        
        self.entries = []
        for entry in self.menu.entries:
            self.entries.append(MenuEntryView(entry, 0))
            
    def setSize(self, width, height):
        """ Set the surface size """
        self.width = width
        self.height = height
        
    def draw(self):
        """ Draw the Battle Menu View """
        menuSurface = GetTransparentSurface(self.width, self.height)
        
        for entry in self.entries:
            entrySurface = entry.draw()
            index = self.entries.index(entry)
            xRatio  = self.getXRatio(index)
            yRatio = self.getYRatio(index)
            entryPos = entrySurface.get_rect(centerx=self.width*xRatio, centery=self.height*yRatio)
            menuSurface.blit(entrySurface, entryPos)
        return menuSurface
            
    def update(self):
        """ Do Nothing """
            
    def getXRatio(self, i):
        """ Returns the xRatio of the entry at i """
        return ((i%2)*2+ 1)/4.0
        
    def getYRatio(self, i):
        """ Returns the yRatio of the entry at i """
        return ((i/2)+ 1)/3.0