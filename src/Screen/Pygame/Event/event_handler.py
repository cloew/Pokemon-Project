from Battle.battle_message import BattleMessage
from Pokemon.LevelEvents.learn_attack_event import LearnAttackEvent

from Screen.Pygame.MessageBox.message_box_controller import MessageBoxController

def PerformEvents(eventQueue, controller):
    """ Perform the given events """
    while len(eventQueue) > 0:
        event = eventQueue.popleft()
        PerformEvent(event, controller)

def PerformEvent(event, controller):
    """ Perform the given event """
    if isinstance(event, BattleMessage):
        controller.runController(MessageBoxController(event, controller.screen))
    elif isinstance(event, LearnAttackEvent):
        print "Received Learn Attack Event"