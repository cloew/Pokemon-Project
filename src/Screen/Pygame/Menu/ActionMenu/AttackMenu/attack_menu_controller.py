from Battle.battle_message import BattleMessage
from Battle.Actions.attack_action import AttackAction

from InputProcessor import commands
from Menu.menu import Menu
from Menu.ActionMenu.AttackMenu.attack_menu_entry import AttackMenuEntry

from Screen.Pygame.Menu.ActionMenu.action_menu_widget import ActionMenuWidget
from Screen.Pygame.Menu.ActionMenu.AttackMenu.attack_menu_entry_widget import AttackMenuEntryWidget
from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController

from kao_gui.pygame.pygame_controller import PygameController

class AttackMenuController(PygameController):
    """ Controller for Attack Menu """
    
    def __init__(self, pokemon, targets, environment, screen):
        """ Initialize the Attack Menu """
        self.pokemon = pokemon
        self.targets = targets
        self.environment = environment
        self.action = None
        
        entries = []
        for attack in self.pokemon.getAttacks():
            entries.append(AttackMenuEntry(attack, self.setAction))
        self.menu = Menu(entries, columns=2)
        
        screen.setBottomView(ActionMenuWidget(self.menu, self.getWindow().width*.9, self.getWindow().height*.3, MenuEntryWidget=AttackMenuEntryWidget))
        cmds = {commands.UP:self.menu.up,
                commands.DOWN:self.menu.down,
                commands.LEFT:self.menu.left,
                commands.RIGHT:self.menu.right,
                commands.SELECT:self.menu.enter,
                commands.EXIT:self.stopRunning}
        PygameController.__init__(self, screen, commands=cmds)
                     
    def setAction(self, entry):
        """ Set the Chosen Action """
        if entry.getAttack().currPowerPoints == 0:
            self.runController(MessageBoxController(BattleMessage("No PP left for this attack."), self.screen))
        else:
            self.action = AttackAction(entry.getAttack(), self.pokemon, self.targets[0], self.environment)
            self.stopRunning()