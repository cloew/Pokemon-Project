
class TeleportEvent:
    """ Represents the event to move to a different Zone """
    
    def __init__(self, newZoneName, row, column):
        """ Initialize the Teleport Event """
        self.newZoneName = newZoneName
        self.row = row
        self.column = column