from Menu.box_menu import BoxMenu
from Menu.menu_entry import MenuEntry

from attack_controller import AttackController

class ActionMenu(BoxMenu):
    """ Represents the Battle's Action Menu """

    def __init__(self, userPkmn):
        """ Create the Action Menu for the given Pokemon """
        self.pkmn = userPkmn
        Menu.__init__(self)
    
    def addEntries(self):
        """  """
        self.action = None
        self.entries = [MenuEntry("FIGHT", self.chooseAttack),
                        MenuEntry("SWITCH", self.tempEntryCallback),
                        MenuEntry("ITEM", self.tempEntryCallback),
                        MenuEntry("RUN", self.tempEntryCallback)]
                             
    def tempEntryCallback(self):
        """ Temporary Call back function for Action menu Entries """

    def chooseAttack(self):
        """ Choose an Attack """
        attackController = AttackController(self.pkmn)
        attackController.run()