from InputProcessor import commands
from InputProcessor.input_processor import inputProcessor
from Screen.Console.window import window

class Controller:
    """ Controller base class """
    
    def __init__(self):
        """ Builds the Controller with no commands"""
        self.cmds = {}
        
    def run(self):
        """ Runs the game loop """
        while self.running():
            window.setScreen(self.getCurrentScreen())
            inputProcessor.processInputs(self.cmds)
            self.update()
            window.update()
            
    def getCurrentScreen(self):
        """ Returns the current screen """
        return None 
        
    def running(self):
        """ Return if the controller is still running """
        return False 
        
    def update(self): # May remove in favor of a threaded application
        """ Function to be overridden to perform periodic updates for the model/controller """