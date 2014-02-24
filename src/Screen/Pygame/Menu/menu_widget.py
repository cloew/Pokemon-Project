from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

from kao_gui.pygame.widgets.sized_widget import SizedWidget

class MenuWidget(SizedWidget):
    """ Represents the widget for a Menu """
    
    def __init__(self, menu, width, height, MenuEntryView=MenuEntryView):
        """ Initialize the widget """
        SizedWidget.__init__(self, width, height)
        self.menu = menu
        self.entries = self.buildEntryViews(MenuEntryView=MenuEntryView)
        
    def buildEntryViews(self, MenuEntryView=MenuEntryView):
        """ Build the Entry Views """
        entries = []
        widthPerEntry = self.width/self.columns
        heightPerEntry = self.height/self.rows
        for entry in self.menu.entries:
            entries.append(MenuEntryView(entry, width=widthPerEntry, height=heightPerEntry))
        return entries
        
    def drawSurface(self):
        """ Draw the Widget """
        for entry in self.entries:
            entrySurface = entry.draw()
            row, column = self.menu.getPosition(entry.entry)
            self.drawOnSurface(entrySurface, left=column/self.columns, top=row/self.rows)
        
    @property
    def columns(self):
        return float(self.menu.columns)
        
    @property
    def rows(self):
        return float(self.menu.rows)