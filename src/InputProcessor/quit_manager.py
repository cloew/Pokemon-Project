class QuitManager:
    """ Manages Quit to Desktop State """
    
    def __init__(self):
        """ Initialize the Quit Manager """
        self.quit = False
        
    def quitToDesktop(self):
        """ Quit to the Desktop """
        self.quit = True
        
QuitManager = QuitManager()