from InputProcessor import commands
from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.battle_menu_view import BattleMenuView
from Screen.Pygame.Menu.ActionMenu.AttackMenu.attack_menu_controller import AttackMenuController

class ActionMenuController(Controller):
    """ Controller for Battle Rounds """
    
    def __init__(self, pokemon, battle, screen):
        """ Initialize the Battle Round Controller """
        Controller.__init__(self)
        self.pokemon = pokemon
        self.battle = battle
        self.screen = screen
        
        entries = [TextMenuEntry("Fight", self.chooseAttack),
                   TextMenuEntry("Switch", None),
                   TextMenuEntry("Item", None),
                   TextMenuEntry("Run", None)]
        self.menu = Menu(entries, columns=2)
        
        self.view = BattleMenuView(self.menu)
        self.screen.setBottomView(self.view)
        self.cmds = {commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.LEFT:self.menu.left,
                     commands.RIGHT:self.menu.right,
                     commands.SELECT:self.menu.enter}
                     
    def chooseAttack(self, entry):
        """ Run the Attack Menu Controller """
        attackMenuController = AttackMenuController(self.pokemon, self.screen)
        self.runController(attackMenuController)
        
    def runController(self, controller):
        """ Runs the given controller """
        controller.run()
        self.screen.setBottomView(self.view)