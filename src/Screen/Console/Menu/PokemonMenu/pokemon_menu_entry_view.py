from Screen.Console.Menu.MainMenu.menu_entry_view import MenuEntryView

class PokemonMenuEntryView(MenuEntryView):
    """ Represents an entry of a Pokemon in the menu """
        
    def draw(self, window):
        """ Draws the menu entry """
        format = self.getTerminalFormatting(self.entry.selected, window.terminal)
        return "{0}{1}{t.normal}".format(format, self.entry.getText(), t=window.terminal)
        
    def getTerminalFormatting(self, selected, terminal):
        """ Sets the Boldness of the entry """
        if selected:
            return terminal.reverse
        else:
            return ""