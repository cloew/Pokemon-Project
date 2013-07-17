from InputProcessor import commands
from Screen.Pygame.Controller.controller import Controller

class ActionController(Controller):
    """ Controller for Battle Rounds """
    
    def __init__(self, pokemon, screen):
        """ Initialize the Battle Round Controller """
        Controller.__init__(self)
        self.pokemon = pokemon
        self.screen = screen
        #self.cmds = {commands.SELECT:self.}