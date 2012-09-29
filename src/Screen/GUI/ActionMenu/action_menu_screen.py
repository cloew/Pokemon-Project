from InputProcessor import commands
from Screen.GUI.TrainerMenu.trainer_menu_entry_view import TrainerMenuEntryView

from Screen.GUI.screen import Screen

import pygame

class ActionMenuScreen(Screen):
    """ Action Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.font = pygame.font.SysFont("Times New Roman", 36)

        self.entries = []
        i = 0
        for entry in self.menu.entries:
            self.entries.append(TrainerMenuEntryView(entry, i))
            i += 1
        
    def draw(self, window):
        """ Draw the window """
        for entry in self.entries:
            entry.draw(window)