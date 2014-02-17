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
        
    def drawSurface(self, surface):
        """ Draw the window """
        self.drawMap(surface)
        self.drawBindings(surface)
        
    def drawMap(self, surface):
        """ Draws the map to the window """
        mapSurf = map.draw()
        surface.blit(mapSurf, (0,0))
        
    def drawBindings(self, surface):
        """ Draw Bindings Text """
        yRatio = 5.0
        
        for cmd in self.bindingsOrder:
            self.drawCommand(surface, cmd, yRatio)
            self.drawKeys(surface, cmd, yRatio)
            yRatio += 3
            
    def drawCommand(self, surface, cmd, yRatio):
        """ Draws the command """
        cmdXRatio = 5.0/16
        
        self.font.set_bold(True)
        text = self.font.render(self.menu.cmdStrings[cmd], 1, (10, 10, 10))
        textpos = text.get_rect(right = surface.get_width()*cmdXRatio, centery = surface.get_height()*(yRatio/32))
        surface.blit(text, textpos)
        
    def drawKeys(self, surface, cmd, yRatio):
        """ Draws the binding """
        bindingXRatio = 8.0/16
        
        self.font.set_bold(False)
        text = self.font.render(self.menu.keyBindings[cmd], 1, (10, 10, 10))
        textpos = text.get_rect(left = surface.get_width()*bindingXRatio, centery = surface.get_height()*(yRatio/32))
        surface.blit(text, textpos)