from InputProcessor import bindings
from InputProcessor import commands

import pygame
from pygame.locals import *

from Menu.menu_entry import MenuEntry

class OptionsMenu():
    """ Class to represent the options menu """
    keyStrings = {K_UP:"UP ARROW",
                         K_w:"W",
                         K_DOWN:"DOWN ARROW",
                         K_s:"S",
                         K_LEFT:"LEFT ARROW",
                         K_a:"A",
                         K_RIGHT:"RIGHT ARROW",
                         K_d:"D",
                         K_ESCAPE:"ESCAPE",
                         K_RETURN:"ENTER"}
                         
    def __init__(self):
        """  """
        self.running = True
        self.heading = "Key Bindings"
        self.back = MenuEntry("Back", self.quit)
        self.back.select()
        
        self.keyBindings = self.getBoundKeyStrings()
                             
    def getBoundKeyStrings(self):
        """ Strings for Bound Keys """
        boundKeys = {commands.EXIT:[],
                             commands.UP:[],
                             commands.DOWN:[],
                             commands.LEFT:[],
                             commands.RIGHT:[],
                             commands.SELECT:[],
                             commands.CANCEL:[]}
        
        for key in bindings.keyBindings:
            boundKeys[bindings.keyBindings[key]].append(self.keyStrings[key])
            
        commandKeys = []
        for cmd in boundKeys:
            s = ""
            for binding in boundKeys[cmd]:
                s += binding
                if not binding == boundKeys[cmd][-1]:
                    s += ", "
            commandKeys.append(s)
            
        return commandKeys
        
    def quit(self):
        """ Quits the Open Menu """
        self.running = False
        