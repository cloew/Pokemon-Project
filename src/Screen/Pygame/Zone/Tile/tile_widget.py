from resources.resource_manager import GetImagePath

from kao_gui.pygame.pygame_helper import load_image
from kao_gui.pygame.widgets.sized_widget import SizedWidget

class TileWidget(SizedWidget):
    """ Represents the widget for a Tile """
    filenameToImage = {}
    # tileImage = load_image(GetImagePath("Tiles/tile.png"))
    
    def __init__(self, tile):
        """ Initialize the widget """
        SizedWidget.__init__(self, 16, 32)
        self.tile = tile
        self.tileImage = self.loadImage()
        
    def drawSurface(self):
        """ Draw the Widget """
        self.drawOnSurface(self.tileImage, left=0, bottom=1)
        if self.tile.contents is not None:
            trainerImage = load_image(GetImagePath("Trainers/{0}.png".format(self.tile.contents.getImageBaseName())))
            self.drawOnSurface(trainerImage, left=0, bottom=1)
            
    def loadImage(self):
        """ Load the tile image """
        if self.tile.tileFilename in self.filenameToImage:
            image = self.filenameToImage[self.tile.tileFilename]
        else:
            image = load_image(GetImagePath("Tiles/{0}.png".format(self.tile.tileFilename)))
            self.filenameToImage[self.tile.tileFilename] = image
        return image