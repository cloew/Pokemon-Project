from Screen.GUI.view import View

class MessageBox(View):
    """ Represents a message box on the screen """
    maxChars = 35
    
    def __init__(self, message):
        """ Builds the Message Box with the given message box """
        self.message = message
        self.charsShown = 0
        #self.stringToDisplay = ""
        self.stringToDisplay = self.message.getMessageSlice(self.message.length())
    
    def update(self):
        """ Updates the message box """
        if self.charsShown < self.message.length():
            self.charsShown += 1
            
        self.stringToDisplay = self.message.getMessageSlice(self.charsShown)
        
    def draw(self, window):
        """ Draws the message box """
        max = window.terminal.width-2
        
        lines = []
        hdrLine ="-"*window.terminal.width
        
        line1 = self.getMessageLine(self.stringToDisplay[:self.maxChars], window.terminal.width)
        line2 = self.getMessageLine(self.stringToDisplay[self.maxChars:], window.terminal.width)
        
        lines.append(hdrLine)
        lines.append(line1)
        lines.append(line2)
        lines.append(hdrLine)
        
        return lines, (window.terminal.width, len(lines))
        
    def getMessageLine(self, text, terminalWidth):
        """ Returns a normalize line from a message """
        diff = terminalWidth-2-len(text)
        return "|{0}{1}|".format(text, " "*diff)