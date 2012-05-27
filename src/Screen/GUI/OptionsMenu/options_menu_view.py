from Screen.GUI.MainMenu.scrolling_map import map

class OptionsMenuScreen:
    """ Options Menu screen """
    
    def __init__(self, menu):
        """  """
        
    def update(self):
        """ Update the screen """
        map.update()
        
    def draw(self, window):
        """ Draw the window """
        map.draw(window)