
class View:
    """ Represents a GUI view for a particular element """
    
    def __init__(self):
        """ Build the View """
        
    def update(self):
        """ Updates the contents of the view. Should be overridden in sub-class """
        
    def draw(self):
        """ Returns the surface with view blitted to it. Should be overridden in sub-class """