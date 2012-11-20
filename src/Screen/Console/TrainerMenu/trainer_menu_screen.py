from InputProcessor import commands
from Screen.Console.TrainerMenu.trainer_menu_entry_view import TrainerMenuEntryView

from Screen.Console.screen import Screen
from Screen.Console.MessageBox.message_box import MessageBox
from Battle.battle_message import BattleMessage

class TrainerMenuScreen(Screen):
    """ Trainer Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.entries = []
        for entry in self.menu.entries:
            self.entries.append(TrainerMenuEntryView(entry))
            
        self.selectedIndex = 0
        self.buildMessageBox()
        
    def draw(self, window):
        """ Draw the window """
        self.drawMenuEntries(window)
        self.findNewSelectedIndex()
        self.buildMessageBox()
        
        messageBox, messageBoxSize = self.messageBox.draw(window)
        window.draw(messageBox, (0,window.terminal.height-5))
            
    def drawMenuEntries(self, window):
        """ Draws all Menu Entries """
        menuText = []
        max = self.getMaxLength()
        for entry in self.entries:
            diff = max - len(entry.entry.getText())
            entryText = "{0}{1}{0}".format(" "*(diff/2), entry.draw(window))
            menuText.append(entryText)
        menuSize = (max, len(menuText))
        
        menuPos = self.getCenteredRect(window, menuSize, .5, .5) 
        window.draw(menuText, menuPos)
        
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