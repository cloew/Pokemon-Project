from resources.resource_manager import GetImagePath

from kao_gui.pygame.pygame_helper import load_image
from kao_gui.pygame.pygame_screen import PygameScreen

class ZoneScreen(PygameScreen):
    """ Screen for a Pokemon Zone """
    MAX_ROWS = 30
    MAX_COLUMNS = 40
    
    def __init__(self, playerPerson, zone):
        """ Initialize the Zone Screen """
        PygameScreen.__init__(self)
        self.playerPerson = playerPerson
        self.zone = zone
        
    def drawSurface(self):
        """ Draw the screen """
        tileImage = load_image(GetImagePath("Tiles/tile.png"))
        
        rowRange = self.getRows()
        columnRange = self.getColumns()
        
        for rowIndex in range(self.MAX_ROWS):
            rowNumber = rowRange[rowIndex]
            if not self.hasRow(rowNumber):
                continue
                
            row = self.zone.tiles[rowNumber]
            for columnIndex in range(self.MAX_COLUMNS):
                if not self.hasColumn(rowNumber, columnRange[columnIndex]):
                    continue
                    
                columnNumber = columnRange[columnIndex]
                tile = row[columnNumber]
                self.drawOnSurface(tileImage, left=columnIndex*16.0/self.width, 
                                              top=rowIndex*16.0/self.height)
                if tile.contents is not None:
                    trainerImage = load_image(GetImagePath("Trainers/{0}.png".format(tile.contents.getImageBaseName())))
                    self.drawOnSurface(trainerImage, left=columnIndex*16.0/self.width,
                                                     top=(rowIndex*16.0-8)/self.height)
                
    def getRows(self):
        """ Return the rows to print tiles from """
        playerRow = self.playerPerson.tile.row
        return range(playerRow-self.MAX_ROWS/2, playerRow+self.MAX_ROWS/2)
        
    def getColumns(self):
        """ Return the Columns to print tiles from """
        playerColumn = self.playerPerson.tile.column
        return range(playerColumn-self.MAX_COLUMNS/2, playerColumn+self.MAX_COLUMNS/2)
        
    def hasRow(self, rowNumber):
        """ Return if the row exists in the tiles """
        return rowNumber >= 0 and rowNumber < len(self.zone.tiles)
        
    def hasColumn(self, rowNumber, columnNumber):
        """ Return if the column exists in the tiles """
        return columnNumber >= 0 and columnNumber < len(self.zone.tiles[rowNumber])
    
    def update(self):
        """ Do Nothing """
        