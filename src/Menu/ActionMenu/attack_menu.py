from Menu.box_menu import BoxMenu
from attack_menu_entry import AttackMenuEntry

from Battle.Actions.attack_action import AttackAction

class AttackMenu(BoxMenu):
    """ Represents the Battle's Attack Menu """

    def __init__(self, userPkmn, targets):
        """ Create the Action Menu for the given Pokemon """
        self.pkmn = userPkmn
        self.targets = targets
        self.action = None
        BoxMenu.__init__(self)
    
    def addEntries(self):
        """ Add entries to the Menu """
        self.entries = []
        for attack in self.pkmn.getAttacks():
            self.entries.append(AttackMenuEntry(attack, self.setAction))

    def setAction(self, entry):
        """ Set the Attack Action """
        self.action = AttackAction(entry.getAttack(), self.pkmn, self.targets[0])