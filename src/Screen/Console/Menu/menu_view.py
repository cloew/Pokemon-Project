from menu_entry_view import MenuEntryView

from kao_gui.console.console_widget import ConsoleWidget

class MenuView(ConsoleWidget):
    """ Represents the menu on the main menu screen """
    
    def __init__(self, menu):
        """ Build the menu """
        self.entries = []
        for i in range(len(menu.entries)):
            entryView = MenuEntryView(menu.entries[i])
            self.entries.append(entryView)
        
    def draw(self): 
        """ Draw the menu """
        return self.drawEntries()
        
    def drawEntries(self):
        """ Draws the menu entries on the Menu Surface """
        menuText = []
        max = self.getMaxLength()
        for entry in self.entries:
            diff = max - len(entry.entry.text)
            entryText = "{0}{1}{0}".format(" "*(diff/2), entry.draw())
            menuText.append(entryText)
        return menuText, (max, len(menuText))
        
    def getMaxLength(self):
        """ Returns the max length """
        max = 0
        for entry in self.entries:
            if len(entry.entry.text) > max:
                max = len(entry.entry.text)
        return max