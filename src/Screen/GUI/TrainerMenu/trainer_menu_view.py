from InputProcessor import commands
from Screen.GUI.MainMenu.scrolling_map import map
from Screen.GUI.TrainerMenu.trainer_menu_entry_view import TrainerMenuEntryView

import pygame

class TrainerMenuScreen:
    """ Trainer Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.font = pygame.font.SysFont("Times New Roman", 36)
        
        self.entries = []
        i = 0
        for entry in self.menu.entries:
            self.entries.append(TrainerMenuEntryView(entry, i))
            i += 1
        
    def update(self):
        """ Update the screen """
        map.update()
        
    def draw(self, window):
        """ Draw the window """
        map.draw(window)
        
        for entry in self.entries:
            entry.draw(window)