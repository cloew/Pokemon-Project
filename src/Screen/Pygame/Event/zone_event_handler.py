from core_event_handler import PerformEvent as PerformCoreEvent
from Event.battle_event import BattleEvent
from Event.teleport_event import TeleportEvent
from Zone.zone_factory import ZoneFactory
from Screen.Pygame.Battle.battle_controller import BattleController

def PerformEvents(eventQueue, zoneController):
    """ Perform the given events """
    while len(eventQueue) > 0:
        event = eventQueue.popleft()
        PerformEvent(event, zoneController)
        
def PerformEvent(event, zoneController):
    """ Perform the given event """
    if isinstance(event, BattleEvent):
        zoneController.runController(BattleController(zoneController.playerPerson.trainer, event.trainerToFight))
    elif isinstance(event, TeleportEvent):
        zone = ZoneFactory.getZone(event.newZoneName)
        zoneController.setupZone(event.newZone, event.row, event.column)
    else:
        PerformCoreEvent(event, zoneController)