from InputProcessor import commands
from InputProcessor.pygame_input_processor import inputProcessor
from Screen.Pygame.window import window

class Controller:
    """ Controller base class """
    
    def __init__(self):
        """ Builds the Controller with no commands"""
        
    def run(self):
        """ Runs the game loop """
        while self.running():
            self.checkScreen()
            self.update()
            window.update()
            inputProcessor.processInputs(self.cmds)
            
    def checkScreen(self):
        """ Checks if the screen should be reset """
        if not window.screen == self.screen:
            window.setScreen(self.screen)
        
    def running(self):
        """ Return if the controller is still running """
        return False 
        
    def update(self): # May remove in favor of a threaded application
        """ Function to be overridden to perform periodic updates for the model/controller """