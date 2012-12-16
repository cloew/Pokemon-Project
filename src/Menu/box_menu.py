from Menu.menu import Menu
from Menu.menu_entry import MenuEntry

class BoxMenu(Menu):
    """ Represents a Menu in a Box rather than a Line """
        
    def up(self):
        """ Selects the entry one up from the one highlighted """
        self.changeSelected(-2)
        
    def down(self):
        """ Selects the entry one down from the one highlighted """
        self.changeSelected(2)
        
    def right(self):
        """ Selects the entry one right from the one highlighted """
        if self.isOdd(self.current):
            self.changeSelected(-1)
        else:
            self.changeSelected(1)
        
    def left(self):
        """ Selects the entry one left from the one highlighted """
        if self.isOdd(self.current):
            self.changeSelected(-1)
        else:
            self.changeSelected(1)
        
    def isOdd(self, num):
        """ Returns if the number is odd """
        return (num % 2) == 1