
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
    
def GetOppositeDirection(direction):
    """ Return the opposite direction of the direction given """
    oppositeDirections = {UP:DOWN,
                          DOWN:UP,
                          LEFT:RIGHT,
                          RIGHT:LEFT}
    return oppositeDirections[direction]