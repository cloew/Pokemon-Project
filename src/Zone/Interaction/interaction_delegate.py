
class InteractionDelegate:
    """ Interaction Delegate for Tile Contents """
    
    def __init__(self, message, callback=None):
        """ Initialize the Interaction delegate """
        self.message = message
        self.callback = callback
        
    def setContent(self, content):
        """ Sets the Content """
        self.content = content
        
    def interact(self, direction):
        """ Interact with the trainer """
        if self.callback is not None:
            self.callback(self.content, self.message)