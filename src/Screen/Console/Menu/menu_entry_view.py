from kao_gui.console.console_widget import ConsoleWidget
from kao_gui.console.window import Window

class MenuEntryView(ConsoleWidget):
    """ Represents an entry in the menu """
    
    def __init__(self, entry):
        """ Sets the entry's text """
        self.entry = entry
        
    def draw(self):
        """ Draws the menu entry """
        format = self.getTerminalFormatting(self.entry.selected, Window.terminal)
        return "{0}{1}{t.normal}".format(format, self.entry.getText(), t=Window.terminal)
        
    def getTerminalFormatting(self, selected, terminal):
        """ Sets the Boldness of the entry """
        if selected:
            return terminal.reverse
        else:
            return ""