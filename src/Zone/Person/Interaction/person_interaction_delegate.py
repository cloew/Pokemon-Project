from Zone.direction import GetOppositeDirection
from Zone.Interaction.interaction_delegate import InteractionDelegate

class PersonInteractionDelegate(InteractionDelegate):
    """ Interaction Delegate for a Zone Person """
        
    def interact(self, direction):
        """ Interact with the trainer """
        self.content.movementDelegate.direction = GetOppositeDirection(direction)
        InteractionDelegate.interact(self, direction)