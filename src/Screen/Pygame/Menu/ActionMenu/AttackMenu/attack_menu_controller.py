from InputProcessor import commands
from Menu.menu import Menu
from Menu.ActionMenu.AttackMenu.attack_menu_entry import AttackMenuEntry
from Screen.Pygame.Controller.controller import Controller
from Screen.Pygame.Menu.battle_menu_view import BattleMenuView

class AttackMenuController(Controller):
    """ Controller for Attack Menu """
    
    def __init__(self, pokemon, screen):
        """ Initialize the Attack Menu """
        Controller.__init__(self)
        self.pokemon = pokemon
        self.screen = screen
        
        entries = []
        for attack in self.pokemon.getAttacks():
            entries.append(AttackMenuEntry(attack, self.setAction))
        self.menu = Menu(entries, columns=2)
        
        self.screen.setBottomView(BattleMenuView(self.menu))
        self.cmds = {commands.UP:self.menu.up,
                     commands.DOWN:self.menu.down,
                     commands.LEFT:self.menu.left,
                     commands.RIGHT:self.menu.right,
                     commands.SELECT:self.menu.enter,
                     commands.EXIT:self.stopRunning}
                     
    def setAction(self, entry):
        """ Set the Chosen Action """