from Screen.Console.view import View
from Screen.Console.Menu.MainMenu.menu_entry_view import MenuEntryView

class PokemonMenuColumn(View):
    """ Represents a column of Pokemon entries on the Pokemon menu screen """
    
    def __init__(self, entries):
        """ Build the Column """
        self.entries = entries
        
    def draw(self, window): 
        """ Draw the menu """
        return self.drawEntries(window)
        
    def drawEntries(self, window):
        """ Draws the menu entries on the Menu Surface """
        menuText = []
        width = 0
        for entry in self.entries:
            entryLines, entrySize = entry.draw(window)
            width = entrySize[0]
            menuText += entryLines
            # diff = max - entry.entry.getTextLength()
            # entryText = "{0}{1}{0}".format(" "*(diff/2), entry.draw(window))
            # menuText.append(entryText)
        return menuText, (width, len(menuText))
        
    # def getMaxLength(self):
    #     """ Returns the max length """
    #     max = 0
    #     for entry in self.entries:
    #         length = entry.entry.getTextLength()
    #         if length > max:
    #             max = length
    #     return max