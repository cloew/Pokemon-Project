
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def GetTextFromDirection(direction):
    """ Returns the text form of a direction """
    directionToText = {UP:"up",
                       DOWN:"down",
                       LEFT:"left",
                       RIGHT:"right"}
    return directionToText[direction]