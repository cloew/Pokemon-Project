class OptionsMenu:
    """ Class to represent the options menu """
    
    def __init__(self):
        """ Build the main menu """
        self.running = True
        
    def quit(self):
        """ Quits the game """
        self.running = False
        