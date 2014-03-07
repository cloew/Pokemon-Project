from resources.resource_manager import GetImagePath

from kao_gui.pygame.pygame_helper import load_image, GetTransparentSurface
from kao_gui.pygame.widgets.image import Image
from kao_gui.pygame.widgets.sized_widget import SizedWidget

from pygame import Surface

class MenuBackgroundWidget(SizedWidget):
    """ Represents the widget for a Menu Background """
    cornerImage = Image(GetImagePath("Menu/pokeball_corner.png"))
    
    def __init__(self, width, height):
        """ Initialize the widget """
        SizedWidget.__init__(self, width, height)
        self.background = GetTransparentSurface(width-6, height-6)
        self.background.fill((3, 60, 176, 127))
        self.horizontalBar = Surface((width-6, 4))
        self.verticalBar = Surface((4, height-6))
        
    def drawSurface(self):
        """ Draw the Widget """
        self.drawOnSurface(self.background, left=(3.0/self.width), top=(3.0/self.height))
        
        self.drawOnSurface(self.horizontalBar, left=(3.0/self.width), top=(3.0/self.height))
        self.drawOnSurface(self.horizontalBar, left=(3.0/self.width), bottom=((self.height-3.0)/self.height))
        
        self.drawOnSurface(self.verticalBar, left=(3.0/self.width), top=(3.0/self.height))
        self.drawOnSurface(self.verticalBar, right=((self.width-3.0)/self.width), top=(3.0/self.height))
        
        cornerImageSurface = self.cornerImage.draw()
        self.drawOnSurface(cornerImageSurface, left=0, top=0)
        self.drawOnSurface(cornerImageSurface, left=0, bottom=1)
        self.drawOnSurface(cornerImageSurface, right=1, top=0)
        self.drawOnSurface(cornerImageSurface, right=1, bottom=1)