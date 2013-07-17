from InputProcessor import commands
from Screen.Pygame.screen import Screen
from Screen.Pygame.Menu.MainMenu.scrolling_map import map

import pygame

class OptionsMenuScreen(Screen):
    """ Options Menu screen """
    bindingsOrder = [commands.EXIT, commands.UP, commands.DOWN, commands.LEFT, commands.RIGHT, commands.SELECT, commands.CANCEL]
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.font = pygame.font.SysFont("Times New Roman", 36)
        
    def update(self):
        """ Update the screen """
        map.update()
        
    def draw(self, window):
        """ Draw the window """
        self.drawMap(window)
        self.drawBindings(window)
        
    def drawMap(self, window):
        """ Draws the map to the window """
        mapSurf = map.draw()
        window.draw(mapSurf, (0,0))
        
    def drawBindings(self, window):
        """ Draw Bindings Text """
        yRatio = 5.0
        
        for cmd in self.bindingsOrder:
            self.drawCommand(window, cmd, yRatio)
            self.drawKeys(window, cmd, yRatio)
            yRatio += 3
            
    def drawCommand(self, window, cmd, yRatio):
        """ Draws the command """
        cmdXRatio = 5.0/16
        
        self.font.set_bold(True)
        text = self.font.render(self.menu.cmdStrings[cmd], 1, (10, 10, 10))
        textpos = text.get_rect(right = window.width*cmdXRatio, centery= window.height*(yRatio/32))
        window.draw(text, textpos)
        
    def drawKeys(self, window, cmd, yRatio):
        """ Draws the binding """
        bindingXRatio = 8.0/16
        
        self.font.set_bold(False)
        text = self.font.render(self.menu.keyBindings[cmd], 1, (10, 10, 10))
        textpos = text.get_rect(left = window.width*bindingXRatio, centery= window.height*(yRatio/32))
        window.draw(text, textpos)