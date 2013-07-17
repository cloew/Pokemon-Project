from Screen.GUI.screen import Screen
from Screen.GUI.MessageBox.message_box import MessageBox

class BattleScreen(Screen):
    """ View for the Battle """
    
    def __init__(self, battle):
        """ Builds the Battle View with the Battle """
        self.messageBox = MessageBox("")
        self.battle = battle
        
    def update(self):
        """ Update the screen """
        if not self.battle.noMessages() and not self.battle.messageQueue[0] == self.messageBox.message:
            self.messageBox = MessageBox(self.battle.messageQueue[0])
        self.messageBox.update()
        
    def draw(self, window):
        """ Draw the window """
        window.clear()
        text = self.messageBox.draw()
        textpos = text.get_rect(left = window.width/20, centery= 3*window.height/4)
        window.draw(text, textpos)