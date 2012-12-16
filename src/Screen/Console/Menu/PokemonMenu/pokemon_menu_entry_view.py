from Screen.Console.Menu.MainMenu.menu_entry_view import MenuEntryView

class PokemonMenuEntryView(MenuEntryView):
    """ Represents an entry of a Pokemon in the menu """
        
    def draw(self, window):
        """ Draws the menu entry """
        format = self.getTerminalFormatting(self.entry.selected, window.terminal)
        pkmn = self.entry.getPokemon()
        return "{0}{1}--{2}{t.normal}".format(format, pkmn.name, pkmn.species, t=window.terminal)

    def getEntrySize(self, window):
        """ Return the entry size """
        return (window.width/2 - 2, window.height/3 - 2)

    def getEntryLines(self, window):
        """ Return entry lines """
        lines = []
        entrySize = self.getEntrySize(window)

        lines.append(self.getHeaderLine())
        lines.append(self.getPokemonNameLine())
        lines.append(self.getHealthLine())
        for i in range(entrySize[1]-4):
            lines.append("")
        lines.append(self.getHeaderLine())
        return lines
        
    def getHeaderLine(self, entrySize):
        """ Returns the line for the header and footer of the entry """
        return "|{0}|".format("-"*(entrySize[0]-2))

    def getLine(self, text, window):
        """ Returns a line """
        entrySize = self.getEntrySize(window)
        spacer = " "*(entrySize[0]-2-len(text))
        format = self.getTerminalFormatting(self.entry.selected, window.terminal)
        return "|{0}{1}{2}{t.normal}|".format(format, text, spacer t=window.terminal)

    def getPokemonNameLine(self):
        """ Returns the Pokemon Name and Species as a string """
        pkmn = self.entry.getPokemon()
        nameString = "{0} --- {1}".format(self.getFullString(pkmn.name), self.getFullString(pkmn.species))
        return self.getLine(nameString)

    def getHealthLine(self):
        """ Return the line with health stats """
        pkmn = self.entry.getPokemon()
        return self.getLine("{0}/{1}".format(pkmn.getCurrHP(), pkmn.getStat("HP")))

    def getFullString(self, string):
        """ Returns a string with the full 10 char limit """
        return (string + " "*10)[:10]

    def getTerminalFormatting(self, selected, terminal):
        """ Sets the Boldness of the entry """
        if selected:
            return terminal.reverse
        else:
            return ""