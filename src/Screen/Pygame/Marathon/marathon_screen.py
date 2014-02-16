from Screen.Pygame.pygame_helper import load_image
from Screen.Pygame.screen import Screen

class MarathonScreen(Screen):
    """ Screen for a Pokemon Marathon """
    
    def __init__(self, marathon):
        """ Initialize the Marathon Screen """
        self.marathon = marathon
        
    def draw(self, window):
        """ Draw the screen """
        window.clear()
        backgroundImage = load_image("Marathons/Kanto_Gym_Leaders.jpg")
        
        window.draw(backgroundImage, (0, 0))
                    
    def update(self):
        """ Do Nothing """