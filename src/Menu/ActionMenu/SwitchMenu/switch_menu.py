from Menu.box_menu import BoxMenu
from Menu.text_menu_entry import TextMenuEntry

from Menu.ActionMenu.AttackMenu.attack_controller import AttackController

class SwitchMenu(BoxMenu):
    """ Represents the Battle's Switch Menu """

    def __init__(self, userPkmn, targets):
        """ Create the Action Menu for the given Pokemon """
        self.pkmn = userPkmn
        self.targets = targets
        self.action = None
        BoxMenu.__init__(self)
    
    def addEntries(self):
        """ Add Menu Entries """
        self.entries = [TextMenuEntry("Pokemon 1", self.tempEntryCallback),
                        TextMenuEntry("Pokemon 2", self.tempEntryCallback),
                        TextMenuEntry("Pokemon 3", self.tempEntryCallback),
                        TextMenuEntry("Pokemon 4", self.tempEntryCallback)]
                             
    def tempEntryCallback(self, entry):
        """ Temporary Call back function for Action menu Entries """

    def chooseAttack(self, entry):
        """ Choose an Attack """
        attackController = AttackController(self.pkmn, self.targets)
        attackController.run()
        self.action = attackController.menu.action