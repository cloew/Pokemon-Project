from core_event_handler import PerformEvent as PerformCoreEvent
from Event.battle_event import BattleEvent
from Screen.Pygame.Battle.battle_controller import BattleController

def PerformEvents(eventQueue, controller):
    """ Perform the given events """
    while len(eventQueue) > 0:
        event = eventQueue.popleft()
        PerformEvent(event, controller)
        
def PerformEvent(event, controller):
    """ Perform the given event """
    if isinstance(event, BattleEvent):
        controller.runController(BattleController(controller.playerPerson.trainer, event.trainerToFight))
    else:
        PerformCoreEvent(event, controller)