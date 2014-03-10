from entry_delegate import EntryDelegate
from Event.teleport_event import TeleportEvent

class TeleportEntryDelegate(EntryDelegate):
    """ Represents a square that teleports the user to a new position """
    
    def __init__(self, zoneName, row, column):
        """ Initialize the Teleport Entry Delegate """
        self.zoneName = zoneName
        self.row = row
        self.column = column
        EntryDelegate.__init__(self)
    
    def onEnter(self, player):
        """ Perform on Enter event """
        self.callback([TeleportEvent(self.zoneName, self.row, self.column)])