from InputProcessor import commands
from Screen.Pygame.screen import Screen
from Screen.Pygame.Menu.MainMenu.scrolling_map import map

from kao_gui.pygame.pygame_screen import PygameScreen

import pygame

class OptionsMenuScreen(PygameScreen):
    """ Options Menu screen """
    bindingsOrder = [commands.EXIT, commands.UP, commands.DOWN, 
                     commands.LEFT, commands.RIGHT,
                     commands.SELECT, commands.CANCEL]
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.font = pygame.font.SysFont("Times New Roman", 36)
        
    def update(self):
        """ Update the screen """
        map.update()
        
    def drawSurface(self):
        """ Draw the window """
        self.drawMap()
        self.drawBindings()
        
    def drawMap(self):
        """ Draws the map to the window """
        mapSurface = map.draw()
        self.drawOnSurface(mapSurface, left=0, top=0)
        
    def drawBindings(self):
        """ Draw Bindings Text """
        yRatio = 5.0
        
        for cmd in self.bindingsOrder:
            self.drawCommand(cmd, yRatio)
            self.drawKeys(cmd, yRatio)
            yRatio += 3
            
    def drawCommand(self, cmd, yRatio):
        """ Draws the command """
        cmdXRatio = 5.0/16
        
        self.font.set_bold(True)
        text = self.font.render(self.menu.cmdStrings[cmd], 1, (10, 10, 10))
        self.drawOnSurface(text, right=cmdXRatio, centery=yRatio/32)
        
    def drawKeys(self, cmd, yRatio):
        """ Draws the binding """
        bindingXRatio = 8.0/16
        
        self.font.set_bold(False)
        text = self.font.render(self.menu.keyBindings[cmd], 1, (10, 10, 10))
        self.drawOnSurface(text, left=bindingXRatio, centery=yRatio/32)