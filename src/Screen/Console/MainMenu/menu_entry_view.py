
class MenuEntryView:
    """ Represents an entry in the menu """
    
    def __init__(self, entry):
        """ Sets the entry's text """
        self.entry = entry
        
    def draw(self, window):
        """ Draws the menu entry """
        format = self.getTerminalFormatting(self.entry.selected, window.terminal)
        #return format(self.entry.text)
        return "{0}{1}{t.normal}".format(format, self.entry.text, t=window.terminal)
        
    def getTerminalFormatting(self, selected, terminal):
        """ Sets the Boldness of the entry """
        if selected:
            return terminal.reverse
        else:
            return ""