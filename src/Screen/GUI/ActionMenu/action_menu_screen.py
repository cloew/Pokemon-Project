from InputProcessor import commands
from Screen.GUI.MainMenu.menu_entry_view import MenuEntryView

from Screen.GUI.screen import Screen

import pygame

class ActionMenuScreen(Screen):
    """ Action Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.font = pygame.font.SysFont("Times New Roman", 36)

        self.entries = []
        
        for entry in self.menu.entries:
            self.entries.append(MenuEntryView(entry, 0))
        
    def draw(self, window):
        """ Draw the window """
        for entry in self.entries:
            entrySurface = entry.draw()
            index = self.entries.index(entry)
            xRatio  = self.getXRatio(index)
            yRatio = self.getYRatio(index)
            entryPos = entrySurface.get_rect(centerx = window.width*xRatio, centery= window.height*yRatio)
            window.draw(entrySurface, entryPos)
            
    def getXRatio(self, i):
        """ Returns the xRatio of the entry at i """
        return (i%2)+ 1)/3.0
        
    def getYRatio(self, i):
        """ Returns the yRatio of the entry at i """
        return (i/2)+ 3)/5.0