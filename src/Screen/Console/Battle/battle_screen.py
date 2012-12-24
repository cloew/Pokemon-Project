from Screen.Console.screen import Screen
from Screen.Console.MessageBox.message_box import MessageBox
from Screen.Console.Battle.player_side_view import PlayerSideView

from Battle.battle_message import BattleMessage

class BattleScreen(Screen):
    """ View for the Battle """
    
    def __init__(self, battle):
        """ Builds the Battle View with the Battle """
        self.messageBox = MessageBox(BattleMessage(""))
        self.battle = battle
        self.playerSideView = PlayerSideView(battle.playerSide)
        self.oppSideView = PlayerSideView(battle.oppSide)
        
    def update(self):
        """ Update the screen """
        if self.hasMessages() and self.newMessage():
            self.messageBox = MessageBox(self.battle.messageQueue[0])
        self.messageBox.update()
        
    def draw(self, window):
        """ Draw the window """
        self.drawOpponentSide(window)
        self.drawPlayerSide(window)
        self.drawMessageBox(window)

    def drawOpponentSide(self, window):
        """ Draws the Player Side """
        opponentSideLines = self.oppSideView.draw(window)
        window.draw(opponentSideLines, (0, 0))

    def drawPlayerSide(self, window):
        """ Draws the Player Side """
        playerSideLines = self.playerSideView.draw(window)
        window.draw(playerSideLines, (0, window.terminal.height-5-len(playerSideLines)))

    def drawMessageBox(self, window):
        """ Draws the Message Box """
        messageBox, messageBoxSize = self.messageBox.draw(window)
        window.draw(messageBox, (0,window.terminal.height-5))

    def hasMessages(self):
        """ Returns if there are messages in the battle's queue """
        return len(self.battle.messageQueue) > 0

    def newMessage(self):
        """ Returns if the message on the top of the queue 
        is different than the current message """
        return not self.battle.messageQueue[0] == self.messageBox.message