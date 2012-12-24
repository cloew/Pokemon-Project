from Controller.controller import Controller
from InputProcessor import commands

from action_menu import ActionMenu
from Screen.Console.Menu.ActionMenu.action_menu_screen import ActionMenuScreen

class ActionController(Controller):
    """ Controller for selecting a Battle Action """
    
    def __init__(self, user, targets, playerSide, oppSide):
        """ Builds the Action Controller """
        self.menu = ActionMenu(user, targets, playerSide, oppSide)
        self.screen = ActionMenuScreen(self.menu, playerSide, oppSide)
        self.cmds = {commands.SELECT:self.menu.enter,
                     commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.RIGHT:self.menu.right,
                     commands.LEFT:self.menu.left,
                     commands.EXIT:self.exit}
        
    def running(self):
        """ Return whether the controller is still running """
        return self.menu.action is None

    def exit(self):
        """ Exits the program """
        print "Exploding!!!"
        raise Exception("My Exception")