
class Screen:
    """ Represents a screen displayed in the game """
    
    def __init__(self):
        """ Build the Screen """
        
    def update(self):
        """ Update the screen. Should be overridden in sub-class """
        
    def draw(self, window):
        """ Draws the screen to the Window provided. Should be overridden in sub-class """ 
        
    def getCenteredRect(self, window, text, xRatio, yRatio):
        """ Returns a position in that centers the text on the given percentage of the screen """
        width = window.terminal.width
        height = window.terminal.height
        
        centerWidth = xRatio*width
        centerHeight = yRatio*height
        centerWidth -= len(text[0])/2
        centerHeight -= len(text)/2
        return centerWidth, centerHeight