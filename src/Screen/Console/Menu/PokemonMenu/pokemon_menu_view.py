from Screen.Console.view import View
from Screen.Console.Menu.MainMenu.menu_entry_view import MenuEntryView

class PokemonMenuView(View):
    """ Represents the Pokemon menu on the main menu screen """
    
    def __init__(self, menu):
        """ Build the menu """
        self.entries = []
        for i in range(len(menu.entries)):
            entryView = MenuEntryView(menu.entries[i])
            self.entries.append(entryView)
        
    def draw(self, window): 
        """ Draw the menu """
        return self.drawEntries(window)
        
    def drawEntries(self, window):
        """ Draws the menu entries on the Menu Surface """
        menuText = []
        max = self.getMaxLength()
        for entry in self.entries:
            diff = max - len(entry.entry.text)
            entryText = "{0}{1}{0}".format(" "*(diff/2), entry.draw(window))
            menuText.append(entryText)
        return menuText, (max, len(menuText))
        
    def getMaxLength(self):
        """ Returns the max length """
        max = 0
        for entry in self.entries:
            if len(entry.entry.text) > max:
                max = len(entry.entry.text)
        return max