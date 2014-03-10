from Event.battle_event import BattleEvent

from Zone.direction import GetOppositeDirection
from Zone.Interaction.interaction_delegate import InteractionDelegate

class PersonInteractionDelegate(InteractionDelegate):
    """ Interaction Delegate for a Zone Person """
        
    def interact(self, direction):
        """ Interact with the trainer """
        self.content.movementDelegate.direction = GetOppositeDirection(direction)
        events = [self.message]
        if self.content.isBattleable():
            events.append(BattleEvent(self.content.trainer))
        if self.callback is not None:
            self.callback(events)