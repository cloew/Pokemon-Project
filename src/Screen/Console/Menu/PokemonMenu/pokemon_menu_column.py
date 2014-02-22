from kao_gui.console.console_widget import ConsoleWidget

class PokemonMenuColumn(ConsoleWidget):
    """ Represents a column of Pokemon entries on the Pokemon menu screen """
    
    def __init__(self, entries):
        """ Build the Column """
        self.entries = entries
        
    def draw(self): 
        """ Draw the menu """
        return self.drawEntries()
        
    def drawEntries(self):
        """ Draws the menu entries on the Menu Surface """
        menuText = []
        width = 0
        for entry in self.entries:
            entryLines, entrySize = entry.draw()
            width = entrySize[0]
            menuText += entryLines
        return menuText, (width, len(menuText))