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
        """ Select the previous entry """
        if self.current > 0:
            self.changeSelected(-1)
            
    def down(self):
        """ Select the next entry """
        if self.current < len(self.entries)-1:
            self.changeSelected(1)
            
    def enter(self):
        """ Call the selected entry """
        self.entries[self.current].call()
            
    def startGame(self):
        """ Start the game """
        print "Starting game"
        
    def options(self):
        """ Go to the options menu """
        print "Options menu"
        
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