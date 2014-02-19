import os

def GetImagePath(imageFilename):
    """ Returns the current path to the given image resource file """
    return os.path.join(GetImageDirectory(), imageFilename)
    
def GetResourceDirectory():
    """ Returns the path to Resource directory """
    return os.path.dirname(__file__)
    
def GetImageDirectory():
    """ Returns the path to the Images directory """
    return os.path.join(GetResourceDirectory(), "images")