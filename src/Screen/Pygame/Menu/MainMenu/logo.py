from resources.resource_manager import GetImagePath

from kao_gui.pygame.widgets.image import Image

class Logo(Image):
    """ Represents the Logo on the screen """
    
    def __init__(self):
        """ Builds the logo """
        Image.__init__(self, GetImagePath("PkmnLogo.png"))