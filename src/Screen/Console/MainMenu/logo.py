from Screen.Console.view import View

class Logo(View):
    """ Represents the Logo on the screen """
    
    def __init__(self):
        """ Builds the logo """
        self.logo = "Pokemon"
        
    def draw(self, window):
        """ Draws the logo """
        return [window.terminal.yellow(self.logo)]