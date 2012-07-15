import random

import pygame
from pygame.locals import *

from Screen.GUI.screen import Screen
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
        mapSurf = map.draw()
        window.draw(mapSurf, (0,0))
        
    def drawLogo(self, window):
        """ Draws the Logo to the window """
        logoSurf = self.logo.draw()
        logoPos = self.getCenteredRect(window, logoSurf, .5, .25) 
        window.draw(logoSurf, logoPos)
        
    def drawMenu(self, window):
        """ Draws the Menu to the window """
        menuSurf = self.menuView.draw()
        menuPos = self.getCenteredRect(window, menuSurf, .5, 11.0/16) 
        window.draw(menuSurf, menuPos)
        