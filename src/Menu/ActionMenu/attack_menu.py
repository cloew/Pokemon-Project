from action_menu import ActionMenu
from Menu.menu_entry import MenuEntry

class AttackMenu(ActionMenu):
    """ Represents the Battle's Attack Menu """
    FIGHT = 0
    SWITCH = 1
    ITEM = 2
    RUN = 3
    
    def addEntries(self):
        """ Add entries to the Menu """
        self.action = None
        self.entries = [MenuEntry("Attack 1", self.tempEntryCallback),
                        MenuEntry("Attack 2", self.tempEntryCallback),
                        MenuEntry("Attack 3", self.tempEntryCallback),
                        MenuEntry("Attack 4", self.tempEntryCallback)]