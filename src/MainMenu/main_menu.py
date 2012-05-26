from menu_entry import MenuEntry

class MainMenu:
    """ Class to represent the main menu """
    
    def __init__(self):
        """ Build the main menu """
        self.running = True
        
        self.entries = [MenuEntry("Start", self.startGame), 
                             MenuEntry("Options", self.options),
                             MenuEntry("Exit", self.quit)]
        self.current = 0
        self.selectEntry()
        
    def up(self):
        """  """
        if self.current > 0:
            self.changeSelected(-1)
            
    def down(self):
        if self.current < len(self.entries)-1:
            self.changeSelected(1)
            
    def startGame(self):
        """ Start the game """
        
    def options(self):
        """ Go to the options menu """
        
    def quit(self):
        """ Quits the game """
        self.running = False
        
    def changeSelected(self, mod):
        """ Change the highlighted menu entry """
        self.deselectEntry()
        self.current += mod
        self.selectEntry()
        
    def selectEntry(self):
        """ Select the current entry """
        self.entries[self.current].select()
        
    def deselectEntry(self):
        """ Deselect the current entry """
        self.entries[self.current].deselect()