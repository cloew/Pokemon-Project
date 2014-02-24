from resources.resource_manager import GetImagePath
from kao_gui.pygame.widgets.image import Image

class TypeImage(Image):
    """ Represents the image for a Type """
    
    def __init__(self, type):
        """ Initialize the widget """
        Image.__init__(self, GetImagePath("Types/{0}_type.png".format(type.lower())))