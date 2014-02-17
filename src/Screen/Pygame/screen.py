from kao_gui.pygame.window import GetWindow

class Screen:
    """ Represents a screen displayed in the game """
    
    def __init__(self):
        """ Build the Screen """
        
    def update(self):
        """ Update the screen. Should be overridden in sub-class """
        
    def draw(self, window):
        """ Draws the screen to the Window provided. Should be overridden in sub-class """ 
        
    def getCenteredRect(self, window, surface, xRatio, yRatio):
        """ Returns a rect for the surface centered at a x, y ratio of the window """
        window = GetWindow()
        x = window.width*xRatio
        y = window.height*yRatio
        return surface.get_rect(centerx = x, centery= y)