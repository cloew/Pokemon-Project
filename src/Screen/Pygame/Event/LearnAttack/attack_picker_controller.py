from InputProcessor import commands
from Menu.menu import Menu
from Menu.ActionMenu.AttackMenu.attack_menu_entry import AttackMenuEntry

from Screen.Pygame.Event.LearnAttack.attack_picker_screen import AttackPickerScreen
from Screen.Pygame.Menu.ActionMenu.action_menu_widget import ActionMenuWidget
from Screen.Pygame.Menu.ActionMenu.AttackMenu.attack_menu_entry_widget import AttackMenuEntryWidget

from kao_gui.pygame.pygame_controller import PygameController

class AttackPickerController(PygameController):
    """ Controller for picking an attack """
    
    def __init__(self, pokemon, lastScreen):
        """ Initialize the Attack Picker Controller """
        self.pokemon = pokemon
        self.attack = None
        
        entries = []
        for attack in self.pokemon.getAttacks():
            entries.append(AttackMenuEntry(attack, self.pickAttack))
        self.menu = Menu(entries, columns=2)
        menuWidget = ActionMenuWidget(self.menu, self.getWindow().width*.9, self.getWindow().height*.3, MenuEntryWidget=AttackMenuEntryWidget)
        
        screen = AttackPickerScreen(menuWidget, lastScreen)
        cmds = {commands.UP:self.menu.up,
                commands.DOWN:self.menu.down,
                commands.LEFT:self.menu.left,
                commands.RIGHT:self.menu.right,
                commands.SELECT:self.menu.enter,
                commands.EXIT:self.stopRunning}
        PygameController.__init__(self, screen, commands=cmds)
        
    def pickAttack(self, entry):
        """ Set the Chosen Attack """
        self.attack = entry.getAttack()
        self.stopRunning()