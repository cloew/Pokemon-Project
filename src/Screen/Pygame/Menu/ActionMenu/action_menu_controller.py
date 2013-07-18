from InputProcessor import commands
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.ActionMenu.action_menu_view import ActionMenuView

class ActionMenuController(Controller):
    """ Controller for Battle Rounds """
    
    def __init__(self, pokemon, screen):
        """ Initialize the Battle Round Controller """
        Controller.__init__(self)
        self.pokemon = pokemon
        self.screen = screen
        self.screen.setBottomView(ActionMenuView())
        self.cmds = {}