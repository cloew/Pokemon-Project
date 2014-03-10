from Zone.direction import GetOppositeDirection
from Zone.Interaction.interaction_delegate import InteractionDelegate

class PersonInteractionDelegate(InteractionDelegate):
    """ Interaction Delegate for a Zone Person """
        
    def interact(self, direction):
        """ Interact with the trainer """
        self.content.movementDelegate.direction = GetOppositeDirection(direction)
        if self.callback is not None:
            self.callback(self.content, [self.message])