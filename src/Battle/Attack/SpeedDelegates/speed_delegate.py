
class SpeedDelegate:
    """ Determines how quickly an attack performs """
    
    def __init__(self, parent, priority):
        """ Build a speed delegate with the specified priority """
        self.parent = parent
        self.priority = priority