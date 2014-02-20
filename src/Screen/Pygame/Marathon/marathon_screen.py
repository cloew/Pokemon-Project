from resources.resource_manager import GetImagePath

from kao_gui.pygame.pygame_helper import load_image
from kao_gui.pygame.pygame_screen import PygameScreen
from kao_gui.pygame.widgets.label import Label

class MarathonScreen(PygameScreen):
    """ Screen for a Pokemon Marathon """
    
    def __init__(self, marathon):
        """ Initialize the Marathon Screen """
        PygameScreen.__init__(self)
        self.marathon = marathon
        self.backgroundImage = load_image(GetImagePath("Marathons/Kanto_Gym_Leaders.jpg"))
        self.congratsLabel = Label("Congratulations! You Won!")
        self.descriptionLabel = Label(marathon.description)
        
    def drawSurface(self):
        """ Draw the screen """
        self.drawOnSurface(self.backgroundImage, left=0, top=0)
        if self.marathon.beaten():
            labelSurface = self.congratsLabel.draw()
        else:
            labelSurface = self.descriptionLabel.draw()
        self.drawOnSurface(labelSurface, left=.05, centery=.1)
                    
    def update(self):
        """ Do Nothing """