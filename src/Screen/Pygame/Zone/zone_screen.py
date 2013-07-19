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
        trainerImage = load_image("Trainers/{0}.png".format(self.trainer.getImageBaseName()))
        
        for i in range(len(self.zone.tiles)):
            row = self.zone.tiles[i]
            for j in range(len(row)):
                tile = row[j]
                window.draw(tileImage, (i*16, j*16))
                if tile is self.trainer.tile:
                    window.draw(trainerImage, (i*16, j*16-8))
        
    def update(self):
        """ Do Nothing """