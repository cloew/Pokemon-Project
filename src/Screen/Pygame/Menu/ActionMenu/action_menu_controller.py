from InputProcessor import commands
from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.two_column_menu_view import TwoColumnMenuView
from Screen.Pygame.Menu.ActionMenu.AttackMenu.attack_menu_controller import AttackMenuController
from Screen.Pygame.Menu.ActionMenu.SwitchMenu.switch_menu_controller import SwitchMenuController

class ActionMenuController(Controller):
    """ Controller for Battle Rounds """
    
    def __init__(self, pokemon, battle, screen):
        """ Initialize the Battle Round Controller """
        Controller.__init__(self)
        self.pokemon = pokemon
        self.battle = battle
        self.screen = screen
        
        entries = [TextMenuEntry("Fight", self.chooseAttack),
                   TextMenuEntry("Switch", self.switch),
                   TextMenuEntry("Item", None),
                   TextMenuEntry("Run", None)]
        self.menu = Menu(entries, columns=2)
        
        self.view = TwoColumnMenuView(self.menu)
        self.screen.setBottomView(self.view)
        self.cmds = {commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.LEFT:self.menu.left,
                     commands.RIGHT:self.menu.right,
                     commands.SELECT:self.menu.enter}
                     
    def chooseAttack(self, entry):
        """ Run the Attack Menu Controller """
        attackMenuController = AttackMenuController(self.pokemon, self.battle.oppSide.pkmnInPlay, self.battle.environment, self.screen)
        self.runController(attackMenuController)
    
    def switch(self, entry):
        """ Run the Switch Menu Controller """
        switchMenuController = SwitchMenuController(self.pokemon)
        self.runController(switchMenuController)
        
    def runController(self, controller):
        """ Runs the given controller """
        controller.run()
        if controller.action is None:
            self.screen.setBottomView(self.view)
        else:
            self.action = controller.action
            self.stopRunning()