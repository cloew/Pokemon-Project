import pygame

from menu_entry import MenuEntry

class Menu:
    """ Represents the menu on the main menu screen """
    
    def __init__(self):
        """ Build the menu """
        self.entry = MenuEntry("Start Game")
        
    def draw(self, window): 
        """ Draw the menu """
        self.entry.draw(window)
        
    def setBold(self, bold):
        """ Set the boldness of the font """
        self.entry.setBold(bold)