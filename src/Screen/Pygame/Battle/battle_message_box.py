from Screen.Pygame.pygame_helper import GetTransparentSurface
from Screen.Pygame.MessageBox.message_box import MessageBox
import pygame

class BattleMessageBox:
    """ Represents the Message Box for a Battle """
    
    def __init__(self, battle):
        """ Initialize the Battle Message Box """
        self.messageBox = MessageBox("")
        self.battle = battle
        
    def setSize(self, width, height):
        """ Set the surface size """
        self.width = width
        self.height = height
        
    def update(self):
        """ Update the screen """
        if not self.battle.noMessages() and not self.battle.messageQueue[0] == self.messageBox.message:
            self.messageBox = MessageBox(self.battle.messageQueue[0])
        self.messageBox.update()
        
    def draw(self):
        """ Draw the child Message Box """
        surface = GetTransparentSurface(self.width, self.height)
        messageBoxSurface = self.messageBox.draw()
        messageBoxPosition = messageBoxSurface.get_rect(centerx=self.width*.5, centery=self.height*.5)
        surface.blit(messageBoxSurface, messageBoxPosition)
        return surface