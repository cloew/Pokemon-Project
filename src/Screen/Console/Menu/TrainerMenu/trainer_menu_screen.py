from Screen.Console.Menu.menu_entry_view import MenuEntryView

from Screen.Console.MessageBox.message_box import MessageBox
from Battle.battle_message import BattleMessage

from kao_gui.console.console_screen import ConsoleScreen

class TrainerMenuScreen(ConsoleScreen):
    """ Trainer Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.entries = []
        for entry in self.menu.entries:
            self.entries.append(MenuEntryView(entry))
            
        self.selectedIndex = 0
        self.buildMessageBox()
        
    def draw(self):
        """ Draw the window """
        self.drawMenuEntries()
        self.findNewSelectedIndex()
        self.buildMessageBox()
        
        messageBox, messageBoxSize = self.messageBox.draw()
        self.drawAtPosition(messageBox, (0, self.terminal.height-4))
            
    def drawMenuEntries(self):
        """ Draws all Menu Entries """
        menuText = []
        max = self.getMaxLength()
        for entry in self.entries:
            diff = max - len(entry.entry.getText())
            entryText = "{0}{1}{0}".format(" "*(diff/2), entry.draw())
            menuText.append(entryText)
        menuSize = (max, len(menuText))
        
        self.drawCenteredText(menuText, menuSize, .5, .5)
        
    def getMaxLength(self):
        """ Returns the max length """
        max = 0
        for entry in self.entries:
            length = len(entry.entry.getText())
            if length > max:
                max = length
        return max
        
    # Unnecessary MessageBox stuff
    def findNewSelectedIndex(self):
        """ Set the new Selected Index """
        for entry in self.entries:
            if entry.entry.selected:
                self.selectedIndex = self.entries.index(entry)
                break
    
    def buildMessageBox(self):
        """ Builds a Message Box """
        battleMessage = BattleMessage("{0}'s first Pkmn is {1}.".format(self.entries[self.selectedIndex].entry.trainer.name, self.entries[self.selectedIndex].entry.trainer.beltPokemon[0].name))
        self.messageBox = MessageBox(battleMessage)