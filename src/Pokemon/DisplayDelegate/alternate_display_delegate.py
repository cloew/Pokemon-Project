
class AlternateDisplayDelegate:
    """ Represents an alternate Display Delegate """
    
    def __init__(self, display):
        """ Initialize the Alternate Display Delegate """
        self.display = display
        
    def getDisplayImageBaseName(self):
        """ Return the Base Image Name based on the new display item """
        return self.display