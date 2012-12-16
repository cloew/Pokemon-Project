from Menu.menu_entry import MenuEntry

class AttackMenuEntry(MenuEntry):
    """ Represents an entry in the menu """
    
    def __init__(self, attack, callback):
        """ Builds a attack menu entry with its attack """
        self.attack = attack
        MenuEntry.__init__(self, callback)
        
    def getAttack(self):
        """ Returns the entry's attack """
        return self.attack
        
    def getText(self):
        """ Return text to display for the Entry """
        return self.attack.name
        