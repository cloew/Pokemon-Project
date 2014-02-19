from resources.resource_manager import GetImagePath

from kao_gui.pygame.pygame_helper import load_image
from kao_gui.pygame.pygame_screen import PygameScreen

class ZoneScreen(PygameScreen):
    """ Screen for a Pokemon Zone """
    
    def __init__(self, zone):
        """ Initialize the Zone Screen """
        PygameScreen.__init__(self)
        self.zone = zone
        
    def drawSurface(self):
        """ Draw the screen """
        tileImage = load_image(GetImagePath("Tiles/tile.png"))
        
        for rowIndex in range(len(self.zone.tiles)):
            row = self.zone.tiles[rowIndex]
            for columnIndex in range(len(row)):
                tile = row[columnIndex]
                self.drawOnSurface(tileImage, left=columnIndex*16.0/self.width, 
                                              top=rowIndex*16.0/self.height)
                if tile.contents is not None:
                    trainerImage = load_image(GetImagePath("Trainers/{0}.png".format(tile.contents.getImageBaseName())))
                    self.drawOnSurface(trainerImage, left=columnIndex*16.0/self.width,
                                                     top=(rowIndex*16.0-8)/self.height)
                    
    def update(self):
        """ Do Nothing """
        