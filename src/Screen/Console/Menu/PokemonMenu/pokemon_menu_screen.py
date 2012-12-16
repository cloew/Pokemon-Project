from Screen.Console.screen import Screen
from pokemon_menu_column import PokemonMenuColumn
from pokemon_menu_entry_view import PokemonMenuEntryView

class PokemonMenuScreen(Screen):
    """ Represents the Pokemon Menu screen """
    
    def __init__(self, menu):
        """ Build the Pokemon Menu """
        self.menu = menu
        leftEntries = []
        rightEntries = []

        for entry in self.menu.entries:
            if self.menu.entries.index(entry):
                rightEntries.append(PokemonMenuEntryView(entry))
            else:
                leftEntries.append(PokemonMenuEntryView(entry))

        self.leftColumn = PokemonMenuColumn(leftEntries)
        self.rightColumn = PokemonMenuColumn(rightEntries)
        
    def draw(self, window):
        """ Draws the screen to the provided window """
        self.drawLeftColumn(window)
        self.drawRightColumn(window)

    def drawLeftColumn(self, window):
        """ Draw the left column """
        menuText, menuSize = self.leftColumn.draw(window)
        menuPos = self.getCenteredRect(window, menuSize, .33, .5) 
        window.draw(menuText, menuPos)
        
    def drawRightColumn(self, window):
        """ Draw the right column """
        menuText, menuSize = self.rightColumn.draw(window)
        menuPos = self.getCenteredRect(window, menuSize, .66, .5) 
        window.draw(menuText, menuPos)