from kao_gui.console.console_widget import ConsoleWidget

class TrainerMenuEntryView(ConsoleWidget):
    """ Represents an entry in the trainer menu """
    
    def __init__(self, entry):
        """ Sets the entry's text """
        self.entry = entry
        
    def draw(self, window):
        """ Draws the menu entry """
        format = self.getTerminalFormatting(self.entry.selected, self.terminal)
        return "{0}{1}{t.normal}".format(format, self.entry.getText(), t=self.terminal)
        
    def getTerminalFormatting(self, selected):
        """ Sets the Boldness of the entry """
        if selected:
            return self.terminal.reverse
        else:
            return ""