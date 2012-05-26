from InputProcessor import bindings

import pygame
from pygame.locals import *

class InputProcessor:
    """ Class to process input from pygame event queue and convert them to game commands """
    
    def __init__(self):
        """ Builds the input processor """
        
    def processInputs(self, functions):
        """ Process inputs to functions """
        commands = self.convertEventToCommand()
        
        for command in commands:
            if command in functions:
                functions[command]()
        
    def convertEventToCommand(self):
        """ Converts PyGame Events to Game Commands """
        commands = []
        
        for event in pygame.event.get():
            if event.type == QUIT:
                raise Exception()
            elif event.type == KEYDOWN:
                if event.key in bindings.keyBindings:
                    commands.append(bindings.keyBindings[event.key])
        
        return commands