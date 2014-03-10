from entry_delegate import EntryDelegate
from Event.teleport_event import TeleportEvent

class TeleportEntryDelegate(EntryDelegate):
    """ Represents a square that teleports the user to a new position """
    
    def onEnter(self, player):
        """ Perform on Enter event """
        print "Teleporting"
        from Zone.zone_factory import ZoneFactory
        zone = ZoneFactory.getZone("Kanto Gym Leaders Marathon")
        self.callback([TeleportEvent(zone, 0, 0)])