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
        
        for rowIndex in range(len(self.zone.tiles)):
            row = self.zone.tiles[rowIndex]
            for columnIndex in range(len(row)):
                tile = row[columnIndex]
                window.draw(tileImage, (columnIndex*16, rowIndex*16))
                if tile is self.trainer.tile:
                    window.draw(trainerImage, (columnIndex*16, rowIndex*16-8))
        
    def update(self):
        """ Do Nothing """