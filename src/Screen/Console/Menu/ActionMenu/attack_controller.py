from Battle.Actions.attack_action import AttackAction
from Menu.menu import Menu
from Menu.ActionMenu.AttackMenu.attack_menu_entry import AttackMenuEntry
from Screen.Console.Menu.ActionMenu.action_menu_screen import ActionMenuScreen

from kao_console.ascii import ENDL, KAO_UP, KAO_DOWN, KAO_LEFT, KAO_RIGHT
from kao_gui.console.console_controller import ConsoleController

class AttackController(ConsoleController):
    """ Controller for selecting a Battle Attack Action """
    
    def __init__(self, pokemon, targets, battle):
        """ Builds the Attack Controller """
        self.pokemon = pokemon
        self.targets = targets
        self.battle = battle
        self.action = None
        
        entries = []
        for attack in self.pokemon.getAttacks():
            entries.append(AttackMenuEntry(attack, self.setAction))
        self.menu = Menu(entries, columns=2)
        
        screen = ActionMenuScreen(self.menu, battle)
        cmds = {ENDL:self.menu.enter,
                KAO_UP:self.menu.up,
                KAO_DOWN:self.menu.down,
                KAO_RIGHT:self.menu.right,
                KAO_LEFT:self.menu.left}
                     
        ConsoleController.__init__(self, screen, commands=cmds, cancellable=True)
        
    def setAction(self, entry):
        """ Set the Chosen Action """
        self.action = AttackAction(entry.getAttack(), self.pokemon, self.targets[0], self.battle.environment)
        self.stopRunning()