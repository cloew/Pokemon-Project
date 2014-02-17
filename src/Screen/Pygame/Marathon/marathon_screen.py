from Screen.Pygame.pygame_helper import load_image
from Screen.Pygame.screen import Screen

from kao_gui.pygame.pygame_screen import PygameScreen

class MarathonScreen(PygameScreen):
    """ Screen for a Pokemon Marathon """
    
    def __init__(self, marathon):
        """ Initialize the Marathon Screen """
        self.marathon = marathon
        
    def drawSurface(self, surface):
        """ Draw the screen """
        backgroundImage = load_image("Marathons/Kanto_Gym_Leaders.jpg")
        self.drawOnSurface(backgroundImage, left=0, top=0)
                    
    def update(self):
        """ Do Nothing """