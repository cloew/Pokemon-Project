from InputProcessor import commands
from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.battle_menu_view import BattleMenuView

class ActionMenuController(Controller):
    """ Controller for Battle Rounds """
    
    def __init__(self, pokemon, screen):
        """ Initialize the Battle Round Controller """
        Controller.__init__(self)
        self.pokemon = pokemon
        self.screen = screen
        entries = [TextMenuEntry("Fight", None),
                   TextMenuEntry("Switch", None),
                   TextMenuEntry("Item", None),
                   TextMenuEntry("Run", None)]
        self.menu = Menu(entries, columns=2)
        self.screen.setBottomView(BattleMenuView(self.menu))
        self.cmds = {commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.LEFT:self.menu.left,
                     commands.RIGHT:self.menu.right,
                     commands.SELECT:self.menu.enter}