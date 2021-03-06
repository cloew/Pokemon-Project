from InputProcessor import bindings

from kao_console import getch
from kao_console.ascii import *

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
        """ Converts Console Key Events to Game Commands """
        commands = []
        event = getch()
        if event in bindings.keyBindings:
            commands.append(bindings.keyBindings[event])
        
        return commands
        
inputProcessor = InputProcessor()