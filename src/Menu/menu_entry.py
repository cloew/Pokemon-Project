
class MenuEntry:
    """ Represents an entry in the menu """
    
    def __init__(self, text, function):
        """ Builds a menu entry with its text and function to call when finished """
        self.text = text
        self.function = function
        self.selected = False
        
    def call(self):
        """ Calls the function """
        self.function()
        
    def select(self):
        """ Select this entry """
        self.selected = True
        
    def deselect(self):
        """ Deselect this entry """
        self.selected = False
        