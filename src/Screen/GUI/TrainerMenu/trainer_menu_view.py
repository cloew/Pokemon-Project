from InputProcessor import commands
from Screen.GUI.MainMenu.scrolling_map import map

import pygame

class TrainerMenuScreen:
    """ Trainer Menu screen """
    
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