from menu_entry import MenuEntry

class TextMenuEntry(MenuEntry):
    """ Represents an entry in the menu with string text """
    
    def __init__(self, text, callback):
        """ Builds a menu entry with its text and callback function to call when finished """
        self.text = text
        MenuEntry.__init__(self, callback)
        
    def getText(self):
        """ Return the text of the Menu Entry """
        return self.text