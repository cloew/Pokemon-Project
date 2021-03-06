from Screen.Pygame.Menu.menu_entry_widget import MenuEntryWidget
from Screen.Pygame.Pokemon.type_image import TypeImage
from resources.resource_manager import GetImagePath

from kao_gui.pygame.widgets.image import Image
from kao_gui.pygame.widgets.label import Label

class AttackMenuEntryWidget(MenuEntryWidget):
    """ Represents the widget for an Attack Menu Entry """
    
    def __init__(self, entry, width, height):
        """ Initialize the widget """
        MenuEntryWidget.__init__(self, entry, fontSize=28, width=width, height=height)
        self.entry = entry
        
        attack = self.entry.attack
        self.typeImage = TypeImage(attack.type)
        self.ppTextLabel = Label("PP", size=18)
        self.ppValuesLabel = Label("{0}/{1}".format(attack.currPowerPoints, attack.powerPoints), size=18)
        
    def drawSurface(self):
        """ Draw the Widget """
        self.drawOnSurface(self.mainLabel.draw(), centerx=.5, centery=.3)
        self.drawOnSurface(self.typeImage.draw(), centerx=.3, centery=.65)
        self.drawOnSurface(self.ppTextLabel.draw(), left=.5, centery=.65)
        self.drawOnSurface(self.ppValuesLabel.draw(), right=.8, centery=.65)
        