from Menu.box_menu import BoxMenu
from Menu.text_menu_entry import TextMenuEntry

from attack_controller import AttackController

class ActionMenu(BoxMenu):
    """ Represents the Battle's Action Menu """

    def __init__(self, userPkmn, targets):
        """ Create the Action Menu for the given Pokemon """
        self.pkmn = userPkmn
        self.targets = targets
        self.action = None
        BoxMenu.__init__(self)
    
    def addEntries(self):
        """ Add Menu Entries """
        self.entries = [TextMenuEntry("FIGHT", self.chooseAttack),
                        TextMenuEntry("SWITCH", self.tempEntryCallback),
                        TextMenuEntry("ITEM", self.tempEntryCallback),
                        TextMenuEntry("RUN", self.tempEntryCallback)]
                             
    def tempEntryCallback(self):
        """ Temporary Call back function for Action menu Entries """

    def chooseAttack(self):
        """ Choose an Attack """
        attackController = AttackController(self.pkmn, self.targets)
        attackController.run()