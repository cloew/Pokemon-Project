from InputProcessor import commands
from InputProcessor.input_processor import inputProcessor
from Screen.GUI.screen import screen

class Controller:
    """ Controller base class """
    
    def __init__(self):
        """ Builds the Controller with no commands"""
        self.cmds = {}
        
    def run(self):
        """ Runs the game loop """
        while self.running():
            screen.setScreen(self.getCurrentScreen())
            screen.update()
            inputProcessor.processInputs(self.cmds)
            screen.draw()
            
    def getCurrentScreen(self):
        """ Returns the current screen """
        return None 
        
    def running(self):
        """ Return if the controller is still running """
        return False 