
class Menu:
    """ Represents a menu in the game """
    
    def __init__(self, entries=None, columns=1):
        """ Build the menu """
        self.columns = columns
        if entries is None:
            self.addEntries()
        else:
            self.entries = entries
        self.current = 0
        self.selectEntry()
        
    def addEntries(self):
        """ Add Entries to the menu """
        self.entries = []
        
    def addEntry(self, entry):
        """ Add an entry to the window """
        self.entries.append(entry)
        
    def up(self, event=None):
        """ Select the entry up one row"""
        if self.currentRow > 0:
            self.changeSelected(-1*self.columns)
            
    def down(self, event=None):
        """ Select the entry down one row """
        if self.currentRow < self.rows-1:
            self.changeSelected(self.columns)
            
    def left(self, event=None):
        """ Select the entry to the left """
        if self.currentColumn > 0:
            self.changeSelected(-1)
        
    def right(self, event=None):
        """ Select the entry to the right """
        if self.currentColumn < self.columns-1:
            self.changeSelected(1)
            
    def enter(self, event=None):
        """ Call the selected entry """
        if self.entries != []:
            self.entries[self.current].call()
        
    def changeSelected(self, mod):
        """ Change the highlighted menu entry """
        self.deselectEntry()
        self.current += mod
        self.current %= len(self.entries)
        self.selectEntry()
        
    def selectEntry(self):
        """ Select the current entry """
        if self.entries != []:
            self.entries[self.current].select()
        
    def deselectEntry(self):
        """ Deselect the current entry """
        if self.entries != []:
            self.entries[self.current].deselect()
            
    @property
    def currentRow(self):
        """ Return the current row """
        return self.current/self.columns
        
    @property
    def currentColumn(self):
        """ Return the current column """
        return self.current % self.columns
        
    @property
    def rows(self):
        """ Return the number of rows """
        rows = len(self.entries)/self.columns
        if len(self.entries)%self.columns > 0:
            rows += 1
        return rows