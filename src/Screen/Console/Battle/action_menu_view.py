from Screen.Console.MainMenu.menu_entry_view import MenuEntryView

from Screen.Console.view import View
from Screen.Console.screen import Screen

class ActionMenuView(View):
    """ Action Menu View """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.entries = []
        
        for entry in self.menu.entries:
            self.entries.append(MenuEntryView(entry))
        
    def draw(self, window):
        """ Draw the window """
        box = self.getMenuBox(window)
        return self.drawMenuEntries(window, box)

    def getMenuBox(self, window):
        """ Draws the Menu Box """
        lines = []
        hdrLine ="-"*window.terminal.width
        line = "|{0}|".format(" "*(window.terminal.width-2))
        
        lines.append(hdrLine)
        lines.append(line)
        lines.append(line)
        lines.append(hdrLine)
        return lines

    def drawMenuEntries(self, window, box):
        """ Draws all Menu Entries """
        menuText = []
        cols = [.33, .66]

        for entry in self.entries:
            index = self.entries.index(entry)
            col = cols[index%2]
            rowIndex = (index > 1) + 1
            length = len(entry.entry.text)
            
            entryPosition = self.getEntryPosition(length, col, window.terminal.width)
            box[rowIndex] = self.addEntryText(entry, int(entryPosition), window, box[rowIndex])
        return box, (window.terminal.width, len(box))

    def addEntryText(self, entry, position, window, line):
        """ Adds the entry text to a line given and returns it """
        newLine  = line[:position]
        newLine += entry.draw(window)
        newLine += line[position+len(entry.entry.text):]
        return newLine 

    def getEntryPosition(self, entryLength, xRatio, terminalWidth):
        """ Gets the position of an entry """
        centerLocation = xRatio*terminalWidth
        centerLocation -= entryLength/2
        return centerLocation