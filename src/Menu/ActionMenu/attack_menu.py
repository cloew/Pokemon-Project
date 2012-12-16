from Menu.box_menu import BoxMenu
from Menu.text_menu_entry import TextMenuEntry

class AttackMenu(BoxMenu):
    """ Represents the Battle's Attack Menu """

    def __init__(self, userPkmn):
        """ Create the Action Menu for the given Pokemon """
        self.pkmn = userPkmn
        BoxMenu.__init__(self)
    
    def addEntries(self):
        """ Add entries to the Menu """
        self.action = None
        self.entries = []
        for attack in self.pkmn.getAttacks():
            self.entries.append(TextMenuEntry(attack.name, self.tempEntryCallback))

    def tempEntryCallback(self):
        """ Temporary Call back function for Action menu Entries """