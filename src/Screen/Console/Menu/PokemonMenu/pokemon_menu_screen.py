from Screen.Console.screen import Screen
from pokemon_menu_column import PokemonMenuColumn
from pokemon_menu_entry_view import PokemonMenuEntryView

from Screen.Console.Battle.battle_screen import BattleScreen

class PokemonMenuScreen(BattleScreen):
    """ Represents the Pokemon Menu screen """
    
    def __init__(self, menu):
        """ Build the Pokemon Menu """
        self.menu = menu
        leftEntries = []
        rightEntries = []

        for entry in self.menu.entries:
            if self.menu.entries.index(entry)%2:
                print "Right:", entry.getText()
                rightEntries.append(PokemonMenuEntryView(entry))
            else:
                print "Left:", entry.getText()
                leftEntries.append(PokemonMenuEntryView(entry))

        self.leftColumn = PokemonMenuColumn(leftEntries)
        self.rightColumn = PokemonMenuColumn(rightEntries)
        
    def draw(self):
        """ Draws the screen to the provided window """
        self.drawLeftColumn()
        self.drawRightColumn()

    def drawLeftColumn(self):
        """ Draw the left column """
        menuText, menuSize = self.leftColumn.draw()
        self.drawAtPosition(menuText, (1, 0))
        
    def drawRightColumn(self):
        """ Draw the right column """
        menuText, menuSize = self.rightColumn.draw()
        self.drawAtPosition(menuText, (1+self.width/2, 0))