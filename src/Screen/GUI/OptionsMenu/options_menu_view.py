from InputProcessor import commands
from Screen.GUI.MainMenu.scrolling_map import map

import pygame

class OptionsMenuScreen:
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
        map.draw(window)
        
        self.drawBindings(window)
        
        
    def drawBindings(self, window):
        """ Draw Bindings Text """
        yRatio = 5.0
        cmdXRatio = 5.0/16
        
        
        for cmd in self.bindingsOrder:
            self.drawCommand(window, cmd, yRatio)
            self.drawKeys(window, cmd, yRatio)
            
            yRatio += 3
            
    def drawCommand(self, window, cmd, yRatio):
        """ Draws the command """
        cmdXRatio = 5.0/16
        
        self.font.set_bold(True)
        text = self.font.render(self.menu.cmdStrings[cmd], 1, (10, 10, 10))
        textpos = text.get_rect(right = window.get_width()*cmdXRatio, centery= window.get_height()*(yRatio/32))
        window.blit(text, textpos)
        
    def drawKeys(self, window, cmd, yRatio):
        """ Draws the binding """
        bindingXRatio = 8.0/16
        
        self.font.set_bold(False)
        text = self.font.render(self.menu.keyBindings[cmd], 1, (10, 10, 10))
        textpos = text.get_rect(left = window.get_width()*bindingXRatio, centery= window.get_height()*(yRatio/32))
        window.blit(text, textpos)