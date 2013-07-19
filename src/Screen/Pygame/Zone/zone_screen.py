from Screen.Pygame.pygame_helper import load_image
from Screen.Pygame.screen import Screen

class ZoneScreen(Screen):
    """ Screen for a Pokemon Zone """
    
    def __init__(self, zone):
        """ Initialize the Zone Screen """
        self.zone = zone
        
    def draw(self, window):
        """ Draw the screen """
        window.clear()
        tileImage = load_image("Tiles/tile.png")
        
        for rowIndex in range(len(self.zone.tiles)):
            row = self.zone.tiles[rowIndex]
            for columnIndex in range(len(row)):
                tile = row[columnIndex]
                window.draw(tileImage, (columnIndex*16, rowIndex*16))
                if tile.contents is not None:
                    trainerImage = load_image("Trainers/{0}.png".format(tile.contents.getImageBaseName()))
                    window.draw(trainerImage, (columnIndex*16, rowIndex*16-8))
                    
    def update(self):
        """ Do Nothing """
        