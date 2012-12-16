from Controller.controller import Controller
from InputProcessor import commands

from attack_menu import AttackMenu
from Screen.Console.ActionMenu.action_menu_screen import ActionMenuScreen

class AttackController(Controller):
    """ Controller for selecting a Battle Attack Action """
    
    def __init__(self, user):
        """ Builds the Action Controller """
        self.userPkmn = user
        self.menu = AttackMenu(user)
        self.screen = ActionMenuScreen(self.menu)
        self.cmds = {commands.SELECT:self.menu.enter,
                     commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.RIGHT:self.menu.right,
                     commands.LEFT:self.menu.left,
                     commands.EXIT:self.exit}
            
    def getCurrentScreen(self):
        """ Returns the current screen """
        return self.actionScreen
        
    def running(self):
        """ Return if the controller is still running """
        return self.menu.action is None 

    def exit(self):
        """ Exits the program """
        print "Exploding!!!"
        raise Exception("My Exception")