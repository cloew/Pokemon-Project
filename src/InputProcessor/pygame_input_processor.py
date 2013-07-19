from InputProcessor import pygame_bindings as bindings
from InputProcessor.key_states import PRESSED, RELEASED

import pygame
from pygame.locals import *

class InputProcessor:
    """ Class to process input from pygame event queue and convert them to game commands """
    
    def __init__(self):
        """ Builds the input processor """
        self.pressedKeys = set([])
        
    def processInputs(self, functions):
        """ Process inputs to functions """
        commands = self.convertEventToCommand()
        
        for command in commands:
            if command in functions:
                functions[command]()
            elif command[0] in functions and command[1] is PRESSED:
                functions[command[0]]()
        
    def convertEventToCommand(self):
        """ Converts PyGame Events to Game Commands """
        commands = []
        
        for event in pygame.event.get():
            if event.type == QUIT:
                raise Exception()
            elif event.type == KEYUP:
                if event.key in bindings.keyBindings:
                    commands.append((bindings.keyBindings[event.key], RELEASED))
            elif event.type == KEYDOWN:
                if event.key in bindings.keyBindings:
                    commands.append((bindings.keyBindings[event.key], PRESSED))
        
        return commands
        
inputProcessor = InputProcessor()