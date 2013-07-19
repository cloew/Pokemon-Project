from Screen.Pygame.pygame_helper import load_image

class ZoneScreen:
    """ Screen for a Pokemon Zone """
    
    def __init__(self, zone, trainer):
        """ Initialize the Zone Screen """
        self.zone = zone
        self.trainer = trainer
        
    def draw(self, window):
        """ Draw the screen """
        window.clear()
        tileImage = load_image("Tiles/tile.png")
        
        for i in range(len(self.zone.tiles)):
            row = self.zone.tiles[i]
            for j in range(len(row)):
                window.draw(tileImage, (i*16, j*16))
        
    def update(self):
        """ Do Nothing """