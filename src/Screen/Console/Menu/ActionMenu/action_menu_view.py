from Screen.Console.Menu.menu_entry_view import MenuEntryView

# from Screen.Console.view import View
# from Screen.Console.screen import Screen

from kao_gui.console.console_widget import ConsoleWidget

class ActionMenuView(ConsoleWidget):
    """ Action Menu View """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.entries = []
        
        for entry in self.menu.entries:
            self.entries.append(MenuEntryView(entry))
        
    def draw(self):
        """ Draw the window """
        box = self.getMenuBox()
        return self.drawMenuEntries(box)

    def getMenuBox(self):
        """ Draws the Menu Box """
        lines = []
        hdrLine ="-"*self.terminal.width
        line = "|{0}|".format(" "*(self.terminal.width-2))
        
        lines.append(hdrLine)
        lines.append(line)
        lines.append(line)
        lines.append(hdrLine)
        return lines

    def drawMenuEntries(self, box):
        """ Draws all Menu Entries """
        menuText = []
        cols = [.33, .66]

        for entry in self.entries:
            index = self.entries.index(entry)
            col = cols[index%2]
            rowIndex = (index > 1) + 1
            length = entry.entry.getTextLength()
            
            entryPosition = self.getEntryPosition(length, col, self.terminal.width)
            box[rowIndex] = self.addEntryText(entry, int(entryPosition), box[rowIndex])
        return box, (self.terminal.width, len(box))

    def addEntryText(self, entry, position, line):
        """ Adds the entry text to a line given and returns it """
        newLine  = line[:position]
        newLine += entry.draw()
        newLine += line[position+entry.entry.getTextLength():]
        return newLine 

    def getEntryPosition(self, entryLength, xRatio, terminalWidth):
        """ Gets the position of an entry """
        centerLocation = xRatio*terminalWidth
        centerLocation -= entryLength/2
        return centerLocation