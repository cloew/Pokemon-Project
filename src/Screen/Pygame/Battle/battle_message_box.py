from Screen.GUI.MessageBox.message_box import MessageBox

class BattleMessageBox:
    """ Represents the Message Box for a Battle """
    
    def __init__(self, battle):
        """ Initialize the Battle Message Box """
        self.messageBox = MessageBox("")
        self.battle = battle
        
    def update(self):
        """ Update the screen """
        if not self.battle.noMessages() and not self.battle.messageQueue[0] == self.messageBox.message:
            self.messageBox = MessageBox(self.battle.messageQueue[0])
        self.messageBox.update()
        
    def draw(self):
        """ Draw the child Message Box """
        return self.messageBox.draw()