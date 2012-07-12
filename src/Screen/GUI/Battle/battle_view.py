from Screen.GUI.MessageBox.message_box import MessageBox

class BattleView:
    """ View for the Battle """
    
    def __init__(self, battle):
        """ Builds the Battle View with the Battle """
        self.messageBox = MessageBox("")
        self.battle = battle
        
    def update(self):
        """ Update the screen """
        if not self.battle.messageQueue[0] == self.messageBox.message:
            self.messageBox = MessageBox(self.battle.messageQueue[0])
        self.messageBox.update()
        
    def draw(self, window):
        """ Draw the window """
        window.fill((255,255,255))
        text = self.messageBox.draw(window)
        textpos = text.get_rect(left = window.get_width()/20, centery= 3*window.get_height()/4)
        window.blit(text, textpos)