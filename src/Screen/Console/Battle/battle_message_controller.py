from Battle.battle_message import BattleMessage
from Screen.Console.MessageBox.message_box import MessageBox

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

class BattleMessageController(ConsoleController):
    """ Controller for Battle Messages """
    
    def __init__(self, battle, screen):
        """ Initialize the Battle Message Controller """
        self.battle = battle
        self.messageBox = MessageBox(BattleMessage(""))
        screen.messageBox = self.messageBox
        cmds = {ENDL:self.battle.removeMessageFromQueue}
        ConsoleController.__init__(self, screen, commands=cmds)
        
    def performGameCycle(self):
        """ Tells the battle object what to perform """
        if self.hasMessages() and self.newMessage():
            self.screen.messageBox = MessageBox(self.battle.messageQueue[0])
        
        if self.battle.noMessages():
            self.stopRunning()
            
    def hasMessages(self):
        """ Returns if there are messages in the battle's queue """
        return len(self.battle.messageQueue) > 0

    def newMessage(self):
        """ Returns if the message on the top of the queue 
        is different than the current message """
        return not self.battle.messageQueue[0] == self.screen.messageBox.message