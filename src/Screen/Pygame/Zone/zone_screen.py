from Screen.Pygame.MessageBox.message_box import MessageBox
from Screen.Pygame.pygame_helper import load_image
from Screen.Pygame.screen import Screen

class ZoneScreen(Screen):
    """ Screen for a Pokemon Zone """
    
    def __init__(self, zone):
        """ Initialize the Zone Screen """
        self.zone = zone
        self.messageBox = None
        
    def draw(self, window):
        """ Draw the screen """
        window.clear()
        tileImage = load_image("Tiles/tile.png")
        
        for rowIndex in range(len(self.zone.tiles)):
            row = self.zone.tiles[rowIndex]
            for columnIndex in range(len(row)):
                tile = row[columnIndex]
                window.draw(tileImage, (columnIndex*16, rowIndex*16))
                if tile.contents is not None:
                    trainerImage = load_image("Trainers/{0}.png".format(tile.contents.getImageBaseName()))
                    window.draw(trainerImage, (columnIndex*16, rowIndex*16-8))
                    
        if self.isShowingMessage():
            text = self.messageBox.draw()
            textpos = self.getCenteredRect(window, text, .5, .75)
            window.draw(text, textpos)
        
    def update(self):
        """ Update the MEssage Box if necessary """
        if self.isShowingMessage():
            self.messageBox.update()
        
    def showMessage(self, message):
        """ Shows the Message String in a Message Box """
        self.messageBox = MessageBox(message)
        
    def isShowingMessage(self):
        """ Returns if the Zone Screen is actively showing a message """
        return self.messageBox is not None 
    
    def stopShowingMessage(self):
        """ Stops displaying the message """
        self.messageBox = None 