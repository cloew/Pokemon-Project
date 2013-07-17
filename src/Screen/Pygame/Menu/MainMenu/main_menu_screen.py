import random

import pygame
from pygame.locals import *

from Screen.Pygame.screen import Screen
from scrolling_map import map
from logo import Logo
from menu_view import MenuView

class MainMenuScreen(Screen):
    """ Represents the Main Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.logo = Logo()
        self.menuView = MenuView(menu)
        
    def update(self):
        """ Update the screen """
        map.update()
        
    def draw(self, window):
        """ Draws the screen to the provided window """
        self.drawMap(window)
        self.drawLogo(window)
        self.drawMenu(window)
        
    def drawMap(self, window):
        """ Draws the map to the window """
        mapSurface = map.draw()
        window.draw(mapSurface, (0,0))
        
    def drawLogo(self, window):
        """ Draws the Logo to the window """
        logoSurface = self.logo.draw()
        logoPosition = self.getCenteredRect(window, logoSurface, .5, .25) 
        window.draw(logoSurface, logoPosition)
        
    def drawMenu(self, window):
        """ Draws the Menu to the window """
        menuSurface = self.menuView.draw()
        menuPosition = self.getCenteredRect(window, menuSurface, .5, 11.0/16) 
        window.draw(menuSurface, menuPosition)
        