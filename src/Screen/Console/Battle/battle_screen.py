from Screen.Console.screen import Screen
from Screen.Console.MessageBox.message_box import MessageBox

from Battle.battle_message import BattleMessage

class BattleScreen(Screen):
    """ View for the Battle """
    
    def __init__(self, battle):
        """ Builds the Battle View with the Battle """
        self.messageBox = MessageBox(BattleMessage(""))
        self.battle = battle
        
    def update(self):
        """ Update the screen """
        if not self.battle.messageQueue[0] == self.messageBox.message:
            self.messageBox = MessageBox(self.battle.messageQueue[0])
        self.messageBox.update()
        
    def draw(self, window):
        """ Draw the window """
        messageBox, messageBoxSize = self.messageBox.draw(window)
        window.draw(messageBox, (0,window.terminal.height-5))