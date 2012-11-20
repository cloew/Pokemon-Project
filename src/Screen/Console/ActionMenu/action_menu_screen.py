from InputProcessor import commands
from Screen.Console.MainMenu.menu_entry_view import MenuEntryView

from Screen.Console.screen import Screen
from Screen.Console.MessageBox.message_box import MessageBox
from Battle.battle_message import BattleMessage

class ActionMenuScreen(Screen):
    """ Action Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.entries = []
        
        for entry in self.menu.entries:
            self.entries.append(MenuEntryView(entry))
        
    def draw(self, window):
        """ Draw the window """
        self.drawMenuBox(window)
        self.drawMenuEntries(window)

    def drawMenuBox(self, window):
        """ Draws the Menu Box """
        lines = []
        hdrLine ="-"*window.terminal.width
        line = "|{0}|".format(" "*(window.terminal.width-2))
        
        lines.append(hdrLine)
        lines.append(line)
        lines.append(line)
        lines.append(hdrLine)
        window.draw(lines, (0,window.terminal.height-5))

    def drawMenuEntries(self, window):
        """ Draws all Menu Entries """
        menuText = []
        max = self.getMaxLength()
        for entry in self.entries:
            diff = max - len(entry.entry.text)
            entryText = "{0}{1}{0}".format(" "*(diff/2), entry.draw(window))
            menuText.append(entryText)
        menuSize = (max, len(menuText))
        
        menuPos = self.getCenteredRect(window, menuSize, .5, .5) 
        window.draw(menuText, menuPos)

    def getMaxLength(self):
        """ Returns the max length """
        max = 0
        for entry in self.entries:
            length = len(entry.entry.text)
            if length > max:
                max = length
        return max