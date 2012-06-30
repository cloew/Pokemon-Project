from InputProcessor import commands
from Screen.GUI.MainMenu.scrolling_map import map
from Screen.GUI.TrainerMenu.trainer_menu_entry_view import TrainerMenuEntryView

from Screen.GUI.MessageBox.message_box import MessageBox
from Battle.battle_message import BattleMessage

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
            
        
        self.selectedIndex = 0
        self.buildMessageBox()
        
    def update(self):
        """ Update the screen """
        map.update()
        
        if not self.entries[self.selectedIndex].entry.selected:
            self.findNewSelectedIndex()
            self.buildMessageBox()
        
        self.messageBox.update()
        
    def draw(self, window):
        """ Draw the window """
        map.draw(window)
        
        for entry in self.entries:
            entry.draw(window)
            
        self.messageBox.draw(window)
        
    # Unnecessary MessageBox stuff
    def findNewSelectedIndex(self):
        """ Set the new Selected Index """
        for entry in self.entries:
            if entry.entry.selected:
                self.selectedIndex = self.entries.index(entry)
                break
    
    def buildMessageBox(self):
        """ Builds a Message Box """
        battleMessage = BattleMessage("{0}'s first Pkmn is {1}".format(self.entries[self.selectedIndex].entry.trainer.name, self.entries[self.selectedIndex].entry.trainer.beltPokemon[0].name))
        self.messageBox = MessageBox(battleMessage)