from Screen.Console.Menu.menu_entry_view import MenuEntryView
from Screen.Console.HealthBar.health_bar_view import HealthBarView

class PokemonMenuEntryView(MenuEntryView):
    """ Represents an entry of a Pokemon in the menu """

    def __init__(self, entry):
        self.healthBar = HealthBarView(entry.getPokemon())
        MenuEntryView.__init__(self, entry)
        
    def draw(self):
        """ Draws the menu entry """
        return self.getEntryLines(), self.getEntrySize()

    def getEntrySize(self):
        """ Return the entry size """
        return (self.window.width/2 - 2, self.window.height/3 - 2)

    def getEntryLines(self):
        """ Return entry lines """
        lines = []
        entrySize = self.getEntrySize()

        lines.append("")
        lines.append(self.getHeaderLine())
        lines.append(self.getPokemonNameLine())
        lines.append(self.getHealthLine())
        lines.append(self.getHealthBarLine())
        for i in range(entrySize[1]-5):
            lines.append(self.getLine(""))
        lines.append(self.getHeaderLine())
        lines.append("")
        return lines
        
    def getHeaderLine(self):
        """ Returns the line for the header and footer of the entry """
        entrySize = self.getEntrySize()
        return "|{0}|".format("-"*(entrySize[0]-2))

    def getLine(self, text):
        """ Returns a line """
        entrySize = self.getEntrySize()
        spacer = " "*(entrySize[0]-2-len(text))
        format = self.getTerminalFormatting(self.entry.selected)
        return "|{0}{1}{2}{t.normal}|".format(format, text, spacer, t=self.terminal)

    def getPokemonNameLine(self):
        """ Returns the Pokemon Name and Species as a string """
        pkmn = self.entry.getPokemon()
        nameString = "{0} --- {1}".format(self.getFullString(pkmn.name), self.getFullString(pkmn.species))
        return self.getLine(nameString)

    def getHealthLine(self):
        """ Return the line with health stats """
        pkmn = self.entry.getPokemon()
        return self.getLine("{0}/{1}".format(pkmn.getCurrHP(), pkmn.getStat("HP")))

    def getHealthBarLine(self):
        """ Return the line with health bar """
        entrySize = self.getEntrySize()
        healthBarText = self.healthBar.draw(entrySize[0]-2, self.entry.selected)
        return "|{0}|".format(healthBarText)

    def getFullString(self, string):
        """ Returns a string with the full 10 char limit """
        return (string + " "*10)[:10]

    def getTerminalFormatting(self, selected):
        """ Sets the Boldness of the entry """
        if selected:
            return self.terminal.reverse
        else:
            return ""