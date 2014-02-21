from kao_gui.console.console_widget import ConsoleWidget

class MessageBox(ConsoleWidget):
    """ Represents a message box on the screen """
    maxChars = 78
    
    def __init__(self, message):
        """ Builds the Message Box with the given message box """
        self.message = message
        self.charsShown = 0
        self.stringToDisplay = self.message.getMessageSlice(self.message.length())
        
    def draw(self):
        """ Draws the message box """
        self.max = self.terminal.width-2
        
        lines = []
        hdrLine ="-"*self.terminal.width
        
        line1 = self.getMessageLine(self.stringToDisplay[:self.max])
        line2 = self.getMessageLine(self.stringToDisplay[self.max:])
        
        lines.append(hdrLine)
        lines.append(line1)
        lines.append(line2)
        lines.append(hdrLine)
        
        return lines, (self.terminal.width, len(lines))
        
    def getMessageLine(self, text):
        """ Returns a normalize line from a message """
        diff = self.max-len(text)
        return "|{0}{1}|".format(text, " "*diff)