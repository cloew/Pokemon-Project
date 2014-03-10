
class TeleportEvent:
    """ Represents the event to move to a different Zone """
    
    def __init__(self, newZone, row, column):
        """ Initialize the Teleport Event """
        self.newZone = newZone
        self.row = row
        self.column = column