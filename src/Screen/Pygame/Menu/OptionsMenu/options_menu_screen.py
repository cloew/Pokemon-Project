from InputProcessor import commands
from Screen.Pygame.screen import Screen
from Screen.Pygame.Menu.MainMenu.scrolling_map import map

from kao_gui.pygame.pygame_screen import PygameScreen
from kao_gui.pygame.widgets.label import Label

import pygame

class OptionsMenuScreen(PygameScreen):
    """ Options Menu screen """
    bindingsOrder = [commands.EXIT, commands.UP, commands.DOWN, 
                     commands.LEFT, commands.RIGHT,
                     commands.SELECT, commands.CANCEL]
    
    def __init__(self, menu):
        """  """
        PygameScreen.__init__(self)
        self.menu = menu
        self.commandLabels = []
        self.keyLabels = []
        for cmd in self.bindingsOrder:
            self.commandLabels.append(Label(self.menu.cmdStrings[cmd], bold=True))
            self.keyLabels.append(Label(self.menu.keyBindings[cmd]))
        
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
        
        for i in range(len(self.bindingsOrder)):
            self.drawCommand(i, yRatio)
            self.drawKeys(i, yRatio)
            yRatio += 3
            
    def drawCommand(self, index, yRatio):
        """ Draws the command """
        cmdXRatio = 5.0/16
        label = self.commandLabels[index]
        self.drawOnSurface(label.draw(), right=cmdXRatio, centery=yRatio/32)
        
    def drawKeys(self, index, yRatio):
        """ Draws the binding """
        bindingXRatio = 8.0/16
        label = self.keyLabels[index]
        self.drawOnSurface(label.draw(), left=bindingXRatio, centery=yRatio/32)